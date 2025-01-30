from ultralytics import YOLO
import cv2
from config import config

def detect_people(image_path):
    '''
        Detect people in an image using YOLO.

        Args:
            image_path (str): Path to the image file.

        Returns:
            results: List of detected objects.

    '''

    # Load a model
    model = YOLO(config.YOLO_MODEL_PATH) 

    # Load an image
    img = cv2.imread(image_path)

    # Perform object detection looking for people
    results = model.predict(img, classes=[0])

    return results