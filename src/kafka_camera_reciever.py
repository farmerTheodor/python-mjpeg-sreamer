
import os
from kafka import KafkaProducer

class KafkaReceiver():

    def __init__(self):
        kafka_url = os.environ['KAFKA_URL']
        print('Kafka url: ' + kafka_url)
        self.kafka_topic = os.environ['KAFKA_TOPIC']
        self.producer = KafkaProducer(bootstrap_servers=[kafka_url])
        

    def on_frame_bytes_received(self, bytes):
        print('Sending frame to kafka')
        future = self.producer.send(self.kafka_topic, bytes)
