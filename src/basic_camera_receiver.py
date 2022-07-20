
from asyncio import Queue

import cv2
import numpy as np
from asyncio import Queue


class BasicReceiver():

    def __init__(self):
        self._frame_queue = Queue()

    def on_frame_bytes_received(self, jpg_bytes):
        frame = cv2.imdecode(np.frombuffer(jpg_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
        self._frame_queue.put_nowait(frame)

    def get_latest_frame(self):
        return self._frame_queue.get()
