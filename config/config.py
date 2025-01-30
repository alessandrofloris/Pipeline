IMAGE_NAME = "IMG_2993"
IMAGE_EXTENSION = "jpeg"
IMAGE_PATH = "images/" + IMAGE_NAME + "." + IMAGE_EXTENSION
OUTPUT_IMAGE_PATH = f"results/{IMAGE_NAME}_bb.jpeg"

OUTPUT_RESULTS_PATH = f"results/{IMAGE_NAME}_results.json"

YOLO_MODEL_PATH = "models/yolo11x.pt"
#LLAVA_MODEL_NAME = "llava-hf/llava-v1.6-vicuna-13b-hf" 
LLAVA_MODEL_NAME = "models/llava-v1.6-vicuna-13b-hf/" 

CLUSTER_THRESHOLD = 100
IMAGE_RESIZE_WIDTH = 640
IMAGE_RESIZE_HEIGHT = 480

GEMINI_API_KEY = "AIzaSyDkgtvMSiqcS2Mu6fQA8vthqPdrKXZM0V0"

LLAVA_PROMPT = "Describe the activity of each person in the image, their sex and their age."
GEMINI_PROMPT = """From the following text extract the following informations: 

    - the number of individfuals

    - for each individual:

    - describe the activity they are doing using max 5 words

    - determine their sex

    - determine their age range



    When not enough details are avaible write "not enough informations"



    The output format should be the following:

    (number of individuals, [(individual id, activity, age, sex), ...])

    No other text should be produced!\n\n"""

#The output should be a single list, and the format should be the following: