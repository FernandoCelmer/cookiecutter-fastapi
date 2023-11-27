from fastapi import APIRouter
from app.api.v1.endpoints import item

router = APIRouter()
router.include_router(item.router, tags=["Item"])
