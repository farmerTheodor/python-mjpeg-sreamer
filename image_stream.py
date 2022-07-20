import time
import fire
from src.receiver_factory import build_receiver
from src.camera_stream import CameraStream

def setup_image_stream(reciever_type = "basic", camera_url = "http://localhost:1337/stream"):
    reciever = build_receiver(reciever_type)
    cap = CameraStream(reciever)
    cap.start_stream(camera_url)
    print("Started image stream")
    while True:
        time.sleep(10)

if __name__ == '__main__':
    fire.Fire(setup_image_stream)