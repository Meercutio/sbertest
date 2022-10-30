from pydantic import BaseModel, Field


class CalculationBody(BaseModel):
    date: str = Field(..., description='application date', example="31.01.2022")
    periods: int = Field(..., description='number of months on deposit', ge=1, le=60, example=3)
    amount: int = Field(..., description='deposit amount', ge=10_000, le=3_000_000, example=10000)
    rate: float = Field(..., description='deposit interest', ge=1, le=8, example=6)
