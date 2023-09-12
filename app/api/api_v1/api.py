from fastapi import APIRouter

from app.api.api_v1.endpoints import utils, curriculum_vitae

api_router = APIRouter()
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(curriculum_vitae.router, prefix="/curriculum_vitae", tags=["curriculum_vitae"])
