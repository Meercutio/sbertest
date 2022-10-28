from datetime import date
from pydantic import BaseModel


class CalculationResult(BaseModel):
    output_data: dict[str, int] | None
