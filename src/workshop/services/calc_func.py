from ..models import CalculationBody
from datetime import datetime, date
import logging
from dateutil.relativedelta import relativedelta


logger = logging.getLogger("log")
logger.setLevel("INFO")


def calculate_amount(amount: float, rate: float) -> float:
    payment: float = amount
    return round(payment * (1 + rate/12/100), 2)


def main_calculation(body: CalculationBody) -> dict:
    format_time = "%d.%m.%Y"
    start_date: date = datetime.strptime(body.date, format_time)
    periods: int = body.periods
    amount: int = body.amount
    rate: float = body.rate
    tmp_amount: float = amount

    result = {}
    i = 0
    while i < periods:
        temp_data = start_date + relativedelta(months=+i)
        tmp_amount = calculate_amount(tmp_amount, rate)
        result[temp_data.strftime('%d.%m.%Y')] = tmp_amount
        i += 1
    return result
