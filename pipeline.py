from models import yolo, llava, gemini_api
from utils import bounding_box, image_utils, clustering
from config import config
from utils import utils

def process_image(image_path):
    """
    Main pipeline function.
    """

    # 1. Detect people with YOLO
    yolo_results = yolo.detect_people(image_path) 
    
    # 2. Extract bounding boxes
    boxes = bounding_box.extract_boxes(yolo_results)

    # 3. Cluster bounding boxes
    clustered_boxes = clustering.cluster_boxes(boxes, distance_threshold=config.CLUSTER_THRESHOLD) 
    
    # 3.1. Draw bounding boxes
    image = image_utils.draw_boxes(image_path, clustered_boxes)
    image_utils.save_image(image, config.OUTPUT_IMAGE_PATH)

    # 4. Crop images
    cropped_images = []
    for box in clustered_boxes:
        cropped_images.append(image_utils.crop_image(image_path, box))

    # 5. Generate LLaVA descriptions    
    descriptions = llava.generate_descriptions(cropped_images)

    # 6. Merge LLaVA outputs
    merged_description = "\n".join(descriptions) 

    # 6. Get person information from Gemini API
    person_info = gemini_api.get_person_info(merged_description) 

    utils.save_results_as_json(config.LLAVA_PROMPT, config.GEMINI_PROMPT, merged_description, person_info, config.OUTPUT_RESULTS_PATH)

    return person_info
    
if __name__ == "__main__":
    image_path = config.IMAGE_PATH
    result = process_image(image_path)
    #print(result) 