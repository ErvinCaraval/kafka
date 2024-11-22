
WORKDIR /app

COPY costumer.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD python costumer.py && tail -f /dev/null