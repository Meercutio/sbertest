from fastapi import FastAPI, APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from ..models import CalculationBody
from starlette import status
from ..services.calc_func import main_calculation
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse


router = APIRouter(
    prefix='/calc',
)
app = FastAPI()


@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"error": "body"}),
    )


@router.post('/')
def calculation(body: CalculationBody):
    return main_calculation(body)
