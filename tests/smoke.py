"""Teste de integração: executar dentro do container da API, com o banco ativo."""

import asyncio
import json
import os
from urllib.request import urlopen

from sqlalchemy import select, text

from app.database import SessionFactory, engine
from app.models import Document


async def check_database() -> None:
    async with SessionFactory() as session:
        assert await session.scalar(text("SELECT version_num FROM alembic_version")) == "0001"
        document = Document(content="smoke-test", embedding=[1.0, 2.0, 3.0])
        session.add(document)
        await session.flush()
        document_id = document.id
        session.expunge(document)
        loaded = await session.get(Document, document_id)
        assert loaded is not None
        assert list(loaded.embedding) == [1.0, 2.0, 3.0]
        distance = await session.scalar(
            select(Document.embedding.l2_distance([1.0, 2.0, 3.0]))
            .where(Document.id == document_id)
        )
        assert distance == 0.0
        await session.rollback()
        assert await session.get(Document, document_id) is None
    await engine.dispose()


assert os.getuid() != 0, "A aplicação deve executar sem root"
for route in ("/health/live", "/health/ready", "/openapi.json", "/docs"):
    with urlopen(f"http://127.0.0.1:8000{route}", timeout=5) as response:
        assert response.status == 200
        if route == "/health/ready":
            assert json.load(response)["database"] == "ok"
asyncio.run(check_database())
print("OK: HTTP, usuário sem root, migração, persistência e distância vetorial via ORM.")
