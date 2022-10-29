from pydantic import BaseModel, Field, validator, ValidationError
import logging
from starlette import status
from fastapi import HTTPException


logger = logging.getLogger("log")


class CalculationBody(BaseModel):
    date: str = Field(..., description='application date', example="31.01.2022")
    periods: int = Field(..., description='number of months on deposit', ge=1, le=60, example=3)
    amount: int = Field(..., description='deposit amount', ge=10_000, le=3_000_000, example=10000)
    rate: float = Field(..., description='deposit interest', ge=1, le=8, example=6)


    # @validator('periods')
    # def period_restrictions(cls, v):
    #     if v < 1 or v > 60:
    #         raise ValidationError('number of months on deposit must be between 1 and 60')
    #     return v
    #
    # @validator('amount')
    # def amount_restrictions(cls, v):
    #     if v < 10_000 or v > 3_000_000:
    #         raise ValidationError('the amount of the deposit must be from 10,000 to 3 million')
    #     return v
    #
    # @validator('rate')
    # def deposit_restrictions(cls, v):
    #     if v < 1 or v > 8:
    #         raise ValidationError('deposit interest must be from 1 to 8')
    #     return v