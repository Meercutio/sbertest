from fastapi.testclient import TestClient
from starlette import status

from app import app

client = TestClient(app)


def test_valid_data():
    response = client.post(
        "/calc",
        json={
              "date": "31.01.2022",
              "periods": 3,
              "amount": 10000,
              "rate": 6
            },
        )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
            "31.01.2022": 10050,
            "28.02.2022": 10100.25,
            "31.03.2022": 10150.75
        }


def test_invalid_data():
    response = client.post(
        "/calc",
        json={
              "date": "31.01.2022",
              "periods": 3,
              "amount": 10000,
              "rate": 0
            },
        )
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        "error": """1 validation error for Request\nbody -> rate\n  ensure this value is greater than or equal to 1 (type=value_error.number.not_ge; limit_value=1)"""
    }
