from app.domain.entities.code_review import CodeReview

class ReviewOrchestrator:
    def __init__(
        self,
        code_analysis_service,
        retrieval_service,
        llm_review_service,
        finding_validation_service,
        report_service,
    ):
        self.code_analysis_service = code_analysis_service
        self.retrieval_service = retrieval_service
        self.llm_review_service = llm_review_service
        self.finding_validation_service = finding_validation_service
        self.report_service = report_service

    async def execute(self, diff: str) -> CodeReview:
        if not diff.strip():
            raise ValueError("O diff não pode estar vazio.")

        analysis = self.code_analysis_service.analyze(diff)
        context = await self.retrieval_service.retrieve(analysis)
        candidates = await self.llm_review_service.review(
            diff=diff,
            analysis=analysis,
            context=context,
        )

        findings = self.finding_validation_service.validate(
            findings=candidates,
            analysis=analysis,
            context=context,
        )

        return self.report_service.build(findings=findings)