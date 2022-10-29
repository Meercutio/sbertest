from fastapi import APIRouter
from models import CalculationBody
from services.calc_func import main_calculation


router = APIRouter(
    prefix='/calc',
)


@router.post('/')
def calculation(body: CalculationBody):
    return main_calculation(body)
