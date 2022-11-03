from fastapi import APIRouter
from models.calculation import CalculationBody
from services.calc_func import main_calculation


router = APIRouter()


@router.post('/calc')
def calculation(body: CalculationBody):
    return main_calculation(body)
