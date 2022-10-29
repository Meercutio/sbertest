from fastapi import APIRouter
from .calculation import router as router_calc


router = APIRouter()
router.include_router(router_calc)
