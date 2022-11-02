FROM python:3.10

WORKDIR /app

COPY ./ ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

RUN coverage run -m pytest && coverage report -m

CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
