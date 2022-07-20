import threading
import time
import cv2
from cv2 import Mat
from numpy import array
import pytest
from src.basic_camera_receiver import BasicReceiver
from src.camera_stream import CameraStream

class TestCameraStream:

    def setup_method(self):
        self.reciever = BasicReceiver()
        self.cap = CameraStream(self.reciever)
        camera_url = "http://localhost:1337/stream"
        self.cap.start_stream(camera_url)
        time.sleep(1)
    
    def teardown_method(self):
        self.close_stream()

    #region Helper Methods
    def close_stream(self):
        self.cap.close_stream()

    def get_latest_frame(self):
        return self.reciever.get_latest_frame()
    
    #endregion

    #region Tests

    @pytest.mark.timeout(10)
    def test_camera_stream_on_close_stream_next_frame_is_none(self):
        assert threading.active_count() == 2
        self.close_stream()
        assert threading.active_count() == 1

    @pytest.mark.timeout(10)
    def test_camera_stream_has_multiple_frames(self): 
        for i in range(10):   
            frame = self.get_latest_frame()
            assert frame is not None
    #endregion

    