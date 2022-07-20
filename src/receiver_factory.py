
from src.basic_camera_receiver import BasicReceiver
from src.kafka_camera_reciever import KafkaReceiver


def build_receiver(reciever_type):

    if reciever_type == 'kafka':
        return KafkaReceiver()
    elif reciever_type == 'basic':
        return BasicReceiver()
    else:
        raise ValueError('Invalid reciever type')