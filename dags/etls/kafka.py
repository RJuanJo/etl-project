import logging
import time
from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start_producer(merged_data_json):
    logger.info('Starting to produce Kafka messages')
    merged_df = pd.read_json(merged_data_json)

    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092']
    )

    for row in merged_df.to_dict(orient="records"):
        producer.send("apidata", value=row)
        time.sleep(1)
        logger.info(f"Mensaje enviado: {row}")

def start_consumer():
    logger.info('Starting Kafka consumer')
    consumer = KafkaConsumer(
        'apidata',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )

    for message in consumer:
        logger.info(f"Mensaje recibido: {message.value}")

if __name__ == "__main__":
    start_consumer()
