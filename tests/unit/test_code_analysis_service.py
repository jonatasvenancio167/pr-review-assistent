import unittest

from app.domain.enum.change_type import ChangeType
from app.services.code_analysis_service import CodeAnalysisService

class TestCodeAnalysisService(unittest.TestCase):
    def test_identifica_remocao_e_adicao(self):
        diff = (
            "@@ -10,2 +10,3 @@\n"
            " def greet():\n"
            '-    print("Hello")\n'
            '+    name = "Maria"\n'
            '+    print(f"Hello, {name}")\n'
        )

        changes = CodeAnalysisService().analyze(diff)

        self.assertEqual(len(changes), 3)

        removed, first_added, second_added = changes

        self.assertEqual(removed.change_type, ChangeType.removed)
        self.assertEqual(removed.old_line_number, 11)
        self.assertIsNone(removed.new_line_number)

        self.assertEqual(first_added.change_type, ChangeType.added)
        self.assertIsNone(first_added.old_line_number)
        self.assertEqual(first_added.new_line_number, 11)
        self.assertEqual(first_added.content, '    name = "Maria"')

        self.assertEqual(second_added.new_line_number, 12)

    def test_ignora_marcador_de_arquivo_sem_quebra_final(self):
        diff = (
            "@@ -1 +1 @@\n"
            "-old\n"
            "\\ No newline at end of file\n"
            "+new\n"
            "\\ No newline at end of file\n"
        )

        changes = CodeAnalysisService().analyze(diff)

        self.assertEqual([change.content for change in changes], ["old", "new"])
        self.assertEqual(changes[0].old_line_number, 1)
        self.assertEqual(changes[1].new_line_number, 1)

    def test_rejeita_quantidades_incompativeis_com_cabecalho(self):
        for diff in (
            "@@ -1 +1 @@\n",
            "@@ -1,2 +1,2 @@\n context\n",
            "@@ -1 +1 @@\n context\n+extra\n",
        ):
            with self.subTest(diff=diff):
                with self.assertRaisesRegex(ValueError, "quantidade de linhas"):
                    CodeAnalysisService().analyze(diff)

    def test_rejeita_entrada_invalida(self):
        for diff in (
            "",
            "  \n",
            "invalid header\n+new\n",
            "@@ -1 +1 @@\n\n",
            "@@ -1 +1 @@\ninvalid prefix\n",
            "@@ -1 +1 @@\n-old\n+new\n@@ -3 +3 @@\n",
        ):
            with self.subTest(diff=diff):
                with self.assertRaises(ValueError):
                    CodeAnalysisService().analyze(diff)
