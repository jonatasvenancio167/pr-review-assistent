import unittest

from app.domain.entities.code_review import CodeReview
from app.domain.entities.review_finding import ReviewFinding
from app.domain.enum.severity import Severity

class TestCodeReview(unittest.TestCase):
    def create_finding(self) -> ReviewFinding:
        return ReviewFinding(
            file_path="app/main.py",
            line_start=10,
            line_end=12,
            severity=Severity.warning,
            title="Exceção muito abrangente",
            explanation="A captura pode ocultar falhas inesperadas."
        )

    def test_review_sem_apontamentos(self):
        review = CodeReview(summary="Nenhum problema identificado.")

        self.assertFalse(review.has_findings)
        self.assertEqual(review.total_findings, 0)

    def test_review_com_apontamentos(self):
        finding = self.create_finding()
        review = CodeReview(
            summary="Um problema identificado.",
            findings=[finding],
        )

        self.assertTrue(review.has_findings)
        self.assertEqual(review.total_findings, 1)
        self.assertEqual(review.findings[0], finding)

    def test_rejeita_resumo_vazio(self):
        for summary in ("", "   ", "\n\t"):
            with self.subTest(summary=summary):
                with self.assertRaises(ValueError):
                    CodeReview(summary=summary)

    if __name__ == "__main__":
        unittest.main()
    