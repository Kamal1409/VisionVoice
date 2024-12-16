import cv2
from src.process import decode_netout
from src.setting import ANCHORS, IMAGE_HEIGHT, IMAGE_WIDTH

def test_model_on_image(model, image_path = "detect/images/zebra.jpg"):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (IMAGE_WIDTH, IMAGE_HEIGHT)) / 255.0
    image_array = np.expand_dims(resized_image, axis=0)
    yhat = model.predict(image_array)

    boxes = []
    for i in range(len(yhat)):
        boxes += decode_netout(yhat[i][0], ANCHORS[i], net_h=IMAGE_HEIGHT, net_w=IMAGE_WIDTH)

    print(f"Detected boxes: {boxes}")
