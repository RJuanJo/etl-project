from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads
import pandas as pd
import time
from threading import Thread

#Datos
csv_file_path = '../data/merge.csv'  
my_dataframe = pd.read_csv(csv_file_path)

# Configurar el productor de Kafka
def start_producer():
    producer = KafkaProducer(
        value_serializer=lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092']
    )
    for row in my_dataframe.to_dict(orient="records"):
        producer.send("apidata", value=row)  
        time.sleep(3)
        print(f"Mensaje enviado: {row}")

# Configurar el consumidor de Kafka
def start_consumer():
    consumer = KafkaConsumer(
        'apidata',  
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )
    for message in consumer:
        print(f"Mensaje recibido: {message.value}")

if __name__ == "__main__":
    # Crear y empezar hilos para el productor y el consumidor
    producer_thread = Thread(target=start_producer)
    consumer_thread = Thread(target=start_consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()