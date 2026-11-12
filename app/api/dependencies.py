from app.services.code_analysis_service import CodeAnalysisService
from app.services.finding_validation_service import FindingValidationService
from app.services.llm_review_service import LLMReviewService
from app.services.rag.retrieval_service import RetrievalService
from app.services.report_service import ReportService
from app.services.review_orchestrator import ReviewOrchestrator

def get_review_orchestrator() -> ReviewOrchestrator:
    return ReviewOrchestrator(
        code_analysis_service=CodeAnalysisService(),
        retrieval_service=RetrievalService(),
        llm_review_service=LLMReviewService(),
        finding_validation_service=FindingValidationService(),
        report_service=ReportService()
    )