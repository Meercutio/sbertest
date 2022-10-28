from fastapi import APIRouter
from ..models import CalculationBody, CalculationResult
from ..services.calc_func import main_calculation


router = APIRouter(
    prefix='/calc',
)


@router.post('/') #response_model=CalculationResult)
def calculation(body: CalculationBody):
    return main_calculation(body)

