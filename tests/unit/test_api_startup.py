import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import HTTPError, URLError
from urllib.request import ProxyHandler, Request, build_opener


class TestAPIStartup(unittest.TestCase):
    def test_inicia_sem_banco_e_mantem_reviews_desativado(self):
        environment = os.environ.copy()
        environment.update(
            POSTGRES_HOST="127.0.0.1",
            POSTGRES_PORT="1",
            POSTGRES_DB="startup_test",
            POSTGRES_USER="startup_test",
            POSTGRES_PASSWORD="startup-test-only",
        )
        opener = build_opener(ProxyHandler({}))

        with tempfile.TemporaryFile(mode="w+") as output:
            # Herdar o socket evita disputa pela porta entre a escolha e o bind.
            with socket.socket() as listener:
                listener.bind(("127.0.0.1", 0))
                listener.listen()
                base_url = f"http://127.0.0.1:{listener.getsockname()[1]}"
                process = subprocess.Popen(
                    [
                        sys.executable, "-B", "-m", "uvicorn", "app.main:app",
                        "--fd", str(listener.fileno()), "--no-access-log",
                    ],
                    cwd=Path(__file__).resolve().parents[2],
                    env=environment,
                    pass_fds=(listener.fileno(),),
                    stdout=output,
                    stderr=subprocess.STDOUT,
                )

            try:
                deadline = time.monotonic() + 10
                while time.monotonic() < deadline and process.poll() is None:
                    try:
                        with opener.open(base_url + "/health/live", timeout=0.25) as response:
                            self.assertEqual(response.status, 200)
                            self.assertEqual(json.load(response), {"status": "ok"})
                        break
                    except (URLError, TimeoutError):
                        time.sleep(0.05)
                else:
                    output.seek(0)
                    self.fail(f"A API não iniciou:\n{output.read()}")

                with opener.open(base_url + "/docs", timeout=2) as response:
                    self.assertEqual(response.status, 200)
                with opener.open(base_url + "/openapi.json", timeout=2) as response:
                    self.assertEqual(response.status, 200)
                    paths = json.load(response)["paths"]
                self.assertNotIn("/reviews", paths)
                self.assertIn("/health/live", paths)
                self.assertIn("/health/ready", paths)

                request = Request(
                    base_url + "/reviews",
                    data=b'{"diff":"@@ -1 +1 @@\\n-old\\n+new"}',
                    headers={"Content-Type": "application/json"},
                    method="POST",
                )
                with self.assertRaises(HTTPError) as caught:
                    opener.open(request, timeout=2)
                with caught.exception as response:
                    self.assertEqual(response.code, 404)
            finally:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)
