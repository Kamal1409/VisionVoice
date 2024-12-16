from queue import Queue
from threading import Thread
import pyttsx3


class TextSpeaker:
    def __init__(self, queue: Queue = Queue()):
        self.queue = queue
        self.speak_text_thread = Thread(target=self.speak_text)
        self.speak_text_thread.start()

    def speak_text(self):
        while True:
            text = self.queue.get()
            if not text:
                self.queue.put(None)
                break
            pyttsx3.speak(text)

    def add_text_to_queue(self, text):
        self.queue.put(text)

    def stop_speaker(self):
        self.queue.put(None)
        self.speak_text_thread.join()


if __name__ == "__main__":
    speaker = TextSpeaker()
    speaker.add_text_to_queue("Hello, world!")
    speaker.add_text_to_queue("This is a test.")
    speaker.stop_speaker()
