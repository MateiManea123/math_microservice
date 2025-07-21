FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "run.py"]
