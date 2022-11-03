from models.calculation import CalculationBody
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

TIME_FORMAT = "%d.%m.%Y"
MONTH_OF_YEAR = 12  # I don't know what the numbers are, but it's possible
PERCENTAGE = 100  # The same


def calculate_amount(amount: float, rate: float) -> float:
    payment: float = amount
    return round(payment * (1 + rate/MONTH_OF_YEAR/PERCENTAGE), 2)


def main_calculation(body: CalculationBody) -> dict:
    start_date: date = datetime.strptime(body.date, TIME_FORMAT)
    periods: int = body.periods
    amount: int = body.amount
    rate: float = body.rate
    tmp_amount: float = amount

    result = {}
    for i in range(periods):
        temp_data = start_date + relativedelta(months=+i)
        tmp_amount = calculate_amount(tmp_amount, rate)
        result[temp_data.strftime(TIME_FORMAT)] = tmp_amount
    return result
