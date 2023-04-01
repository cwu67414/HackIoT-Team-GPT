import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

picam2.start_recording('test.mp4')
time.sleep(10)
picam2.stop_recording()