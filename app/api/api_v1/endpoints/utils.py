from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def read_health():
    return {"status": "Server is up and running!"}
