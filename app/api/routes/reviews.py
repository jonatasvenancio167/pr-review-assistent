from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.schemas.review_schema import ReviewRequest
from app.services.review_orchestrator import ReviewOrchestrator
from app.api.dependencies import get_review_orchestrator

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("")
async def create_review(
    request: ReviewRequest,
    orchestrator: Annotated[
        ReviewOrchestrator,
        Depends(get_review_orchestrator),
    ],
):
    return await orchestrator.execute(request.diff)
