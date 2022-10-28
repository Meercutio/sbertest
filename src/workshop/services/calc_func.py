from ..models import CalculationBody
from datetime import date, timedelta
import calendar


def iter_month(current_date: date):
    days = calendar.monthrange(current_date.year, current_date.month)[1]
    next_month_date = current_date + timedelta(days=days)
    return next_month_date


def main_calculation(body: CalculationBody):
    start_date: date = body.date
    periods: int = body.periods
    amount: int = body.amount
    rate: int = body.rate
    result = {start_date: amount}
    i = 0
    while i < periods:
        result[start_date + timedelta(days=i)] = amount
        i += 1
    return result
