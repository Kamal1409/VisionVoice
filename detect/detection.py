
from pathlib import Path
from queue import Queue

import cv2
import numpy as np
from keras.api.models import load_model
from keras.api.optimizers import Adam
from src.nmsupress import do_nms
from src.process import box_filter, decode_netout
from src.setting import ANCHORS, IMAGE_HEIGHT, IMAGE_WIDTH, NMS_SCORE
from src.utili import encoder_dic


class Detector:
    def __init__(
        self,
        # model path is set as model/yolov3.h5 where model dir is on same level
        # as this file
        model_path=Path(__file__).parent / "model" / "yolov3.h5",
        text_queue: Queue = Queue()
    ):
        print(f"Loading model from: {model_path}")
        self.text_queue = text_queue
        self.model = load_model(model_path)
        self.model.compile(
            optimizer=Adam(), loss="categorical_crossentropy"
        )  # Compile the model manually
        self.detected_labels = set()  # Set to keep track of detected labels

    def _preprocess_frame(self, frame):
        image_height, image_width = frame.shape[:2]
        frame_resized = cv2.resize(frame, (IMAGE_WIDTH, IMAGE_HEIGHT))  # Resize frame
        frame_normalized = frame_resized / 255.0  # Normalize to [0, 1]
        return frame_normalized, image_width, image_height

    def _predict(self, image):
        image_x = np.expand_dims(image, 0)  # Add batch dimension
        yhat = self.model.predict(image_x)
        return yhat

    def _convert_to_boxes(self, yhat, image_width, image_height):
        boxes = []
        for i in range(len(yhat)):
            boxes += decode_netout(
                yhat[i][0], ANCHORS[i], net_h=IMAGE_HEIGHT, net_w=IMAGE_WIDTH
            )

        # Convert boxes to image scale
        for box in boxes:
            box.xmin = int((box.xmin * image_width) / IMAGE_WIDTH)
            box.xmax = int((box.xmax * image_width) / IMAGE_WIDTH)
            box.ymin = int((box.ymin * image_height) / IMAGE_HEIGHT)
            box.ymax = int((box.ymax * image_height) / IMAGE_HEIGHT)

        return boxes

    def do_detect(self):
        # Initialize webcam
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")

        print("Webcam opened successfully.")

        ret, frame = cap.read()  # Capture a single frame
        if not ret:
            print("Failed to grab frame")
            cap.release()  # Ensure the webcam is released if the frame capture fails

        print("Frame captured successfully.")

        # Preprocess the frame
        image, image_width, image_height = self._preprocess_frame(frame)

        # Perform detection
        yhat = self._predict(image)
        boxes = self._convert_to_boxes(yhat, image_width, image_height)

        dic = encoder_dic(box_filter(boxes))
        valid_data = do_nms(dic, NMS_SCORE)

        # Print only unique labels of detected objects with status "kept"
        for label in valid_data[1]:
            self.text_queue.put(label +"is detected")
            print(f"Detected: {label} is detected")  # Output the label
            self.detected_labels.add(label)  # Add label to the set

        # Release the webcam
        cap.release()


if __name__ == "__main__":
    D = Detector()
    D.do_detect()
