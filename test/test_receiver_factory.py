
from src.basic_camera_receiver import BasicReceiver
from src.kafka_camera_reciever import KafkaReceiver
from src.receiver_factory import build_receiver


def test_on_string_basic_get_basic_receiver():
    receiver = build_receiver('basic') 
    assert type(receiver) is BasicReceiver

def test_on_string_kafka_get_kafka_receiver():
    receiver = build_receiver('kafka') 
    assert type(receiver) is KafkaReceiver

