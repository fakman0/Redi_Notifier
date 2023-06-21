FROM python:3.9

WORKDIR /app

COPY requirements_api.txt .
COPY ../api.py .
COPY ../database.db .


RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "api.py"]
