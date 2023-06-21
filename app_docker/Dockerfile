FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY fn_database.py .
COPY fn_login.py .
COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
