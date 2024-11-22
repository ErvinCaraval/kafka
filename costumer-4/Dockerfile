FROM python:3.9-slim

WORKDIR /app

COPY costumer-4.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD python costumer-4.py && tail -f /dev/null