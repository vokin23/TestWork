FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .

RUN  pip install -r requirements.txt

COPY . .

CMD alembic revision --autogenerate; alembic upgrade head; uvicorn app.main:app --host 0.0.0.0 --port 8000