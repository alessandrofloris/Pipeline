from models import llava, gemini_api, fastrcnn
from utils import bounding_box, image_utils, clustering
from config import config
from utils import utils
import os

def process_image(image_path, filename):
    """
    Main pipeline function.
    """

    # 1. Detect people and get their bounding boxes
    boxes = fastrcnn.detect_people(image_path)

    # 2. Padding bounding boxes 
    boxes = bounding_box.padding_bounding_boxes(boxes, image_path)

    # 3. Cluster bounding boxes
    clustered_boxes = clustering.cluster_boxes(boxes, distance_threshold=config.CLUSTER_THRESHOLD) 
    
    # 3.1 Draw bounding boxes
    image = image_utils.draw_boxes(image_path, clustered_boxes)
    filename_bb = filename.replace(".jpeg", "_bb.jpeg")
    image_utils.save_image(image, config.OUTPUT_IMAGE_PATH + filename_bb)

    # 4. Crop images
    cropped_images = []
    for box in clustered_boxes:
        cropped_images.append(image_utils.crop_image(image_path, box))

    # 5. Generate LLaVA descriptions    
    descriptions = llava.generate_descriptions(cropped_images)

    # 6. Merge LLaVA outputs
    merged_description = str(descriptions)

    # 7. Get person information from Gemini API
    person_info = gemini_api.get_person_info(merged_description) 

    filename_result = filename.replace(".jpeg", "_results.json")
    utils.save_results_as_json(config.LLAVA_PROMPT, config.GEMINI_PROMPT, merged_description, person_info, config.OUTPUT_RESULTS_PATH + filename_result)

    return person_info
    
if __name__ == "__main__":
    #image_path = config.IMAGE_PATH
    image_folder_path = config.IMAGE_FOLDER_PATH
    #result = process_image(image_path)
    for filename in os.listdir(image_folder_path):
        if filename.endswith(".jpeg"):
            image_path = os.path.join(image_folder_path, filename)
            process_image(image_path, filename)
