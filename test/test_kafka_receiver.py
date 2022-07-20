# example using kafka-python
import os
import time
import kafka

from src.kafka_camera_reciever import KafkaReceiver



class TestKafkaReceiver:

    def setup_method(self):
        kafka_server = os.environ['KAFKA_URL']
        kafka_topic = os.environ['KAFKA_TOPIC']
        self.consumer = kafka.KafkaConsumer(kafka_topic,group_id='test', bootstrap_servers=[kafka_server])

    def teardown_method(self):
        self.consumer.close()
        self.consumer = None

    def test_kafka_connection(self):
        assert self.consumer is not None

    def test_kafka_receiver_publishes_to_kafka(self):
        receiver = KafkaReceiver()
        receiver.on_frame_bytes_received(b'hello')
        time.sleep(1)
        message = next(self.consumer)
        assert message.value == b'hello'
        
