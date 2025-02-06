IMAGE_NAME = "IMG_2984"
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

PADDING_BB_X = 0.5
PADDING_BB_Y = 0.3

GEMINI_API_KEY = "AIzaSyDkgtvMSiqcS2Mu6fQA8vthqPdrKXZM0V0"

LLAVA_PROMPT = """For each person in the image try to briefly describe their activity, their presumed age range and their presumed sex."""

GEMINI_PROMPT = """From the following text extract the following informations: 

    - the number of persons
    - for each person:
    - describe the activity they are doing using one of the following (cuddling, standing alone, standing togheter, reading, sleeping, eating/drinking, playing alone, playing togheter, conversation, walking alone, walking in group, playing with pet)
    - determine their sex (male, female)
    - determine their age range (child, adult, senior)

    When not enough details are avaible write "not enough informations"

    The output format should be the following:
    (number of individuals, [(individual id, activity, age, sex), ...])
    No other text should be produced!"""

#The output should be a single list, and the format should be the following: