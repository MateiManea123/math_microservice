import json

from . import db
from kafka import KafkaProducer
from app.monitor import *

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v:json.dumps(v).encode('utf-8')
)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    endpoint = db.Column(db.String(255), nullable = False)
    method = db.Column(db.String(10), nullable = False)
    headers = db.Column(db.Text, nullable = True)
    body = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Post('{self.id}', '{self.endpoint}','{self.method}', '{self.headers}','{self.body}')"


def log_event(message, extra: dict = None):
    log_data ={
        "message" : message,
        "extra" : extra or {}
    }
    try:
        producer.send('logs',log_data)
        producer.flush()
    except Exception as e:
        print("Kafka logging failed:",e)


def add_request(request_got):
    print_usages()
    new_request_db = Request(
        endpoint = request_got.path,
        method = request_got.method,
        headers = str(request_got.headers),
        body = request_got.get_data(as_text=True)
    )
    new_request_kafka = {
        "endpoint" :request_got.path,
        "method": request_got.method,
        "headers": str(request_got.headers),
        "body": request_got.get_data(as_text=True)
    }
    try:
        producer.send('requests',new_request_kafka)
        producer.flush()
    except Exception as e:
        print('Kafka requests failed: ', e)

    db.session.add(new_request_db)
    db.session.commit()
    log_event("Request Stored!", {
        "endpoint":request_got.path,
        "method":request_got.method
    })