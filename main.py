from queue import Queue
from detect import Detector
from tts import TextSpeaker

queue = Queue()
obj_warn = TextSpeaker(queue=queue)
obj_detection = Detector(text_queue=queue)
obj_detection.do_detect()
obj_warn.stop_speaker()
