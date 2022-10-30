FROM python:3.10

WORKDIR /app

COPY ./ ./

RUN pip install --upgrade pip

RUN python3.10 -m venv .env


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN python -m pytest && coverage run -m pytest && coverage report -m


CMD ["uvicorn", "app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
