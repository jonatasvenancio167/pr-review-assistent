from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/", tags=[""])
async def read():
    pass