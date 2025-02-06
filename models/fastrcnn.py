# Some basic setup:
# Setup detectron2 logger
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg

import numpy
import cv2

def detect_people(image_path):
    '''
        Detect people in an image using faster-rcnn.

        Args:
            image_path: Path to the image file.

        Returns: 
            List of bounding boxes.
    '''

    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml"))
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7  # set threshold for this model
    cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-Detection/faster_rcnn_X_101_32x8d_FPN_3x.yaml")
    predictor = DefaultPredictor(cfg)

    try:

        image = cv2.imread(image_path)

        outputs = predictor(image)    

        instances = outputs["instances"] 
        person_indices = instances.pred_classes == 0  # Get indices of person detections

        person_instances = instances[person_indices]

        pred_boxes = person_instances.pred_boxes.tensor.cpu().numpy()

        return pred_boxes

    except Exception as e:
        
        print(f"Error processing {image_path}: {e}")