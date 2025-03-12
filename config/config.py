#IMAGE_NAME = "IMG_2984"
#IMAGE_EXTENSION = "jpeg"
#IMAGE_PATH = f"images/{IMAGE_NAME}.jpeg"
IMAGE_FOLDER_PATH = "images/"
#OUTPUT_IMAGE_PATH = f"results/{IMAGE_NAME}_bb.jpeg"
OUTPUT_IMAGE_PATH = "results/"

#OUTPUT_RESULTS_PATH = f"results/{IMAGE_NAME}_results.json"
OUTPUT_RESULTS_PATH = "results/"

#YOLO_MODEL_PATH = "models/yolo11x.pt"
LLAVA_MODEL_NAME = "llava-hf/llava-v1.6-vicuna-13b-hf" 
#LLAVA_MODEL_NAME = "models/llava-v1.6-vicuna-13b-hf/" 

CLUSTER_THRESHOLD = 100
#IMAGE_RESIZE_WIDTH = 640
#IMAGE_RESIZE_HEIGHT = 480

PADDING_BB_X = 0.5
PADDING_BB_Y = 0.3

GEMINI_API_KEY = "" 

LLAVA_PROMPT = """For each person in the image try to briefly describe their activity and if they seem interacting with someone or are togheter with someone, describe their presumed age range and their presumed sex. Focus only on this details, dont add other informations."""

GEMINI_PROMPT = """From the following list of texts extract the following informations: 

    - the number of persons
    - for each person (be carefull only persons not animals or objects):
    - describe the activity they are doing using one of the following (cuddling, standing alone, standing togheter, smoking, using smartphone, reading, sleeping, eating/drinking, playing alone, playing togheter, conversation, walking alone, walking togheter, playing with pet)
    - determine their sex (male, female)
    - determine their age range (child, adult, senior)

    When not enough details are avaible write "not enough informations"

    You should output a single tuple and the format should be the following:
    (number of individuals, [(id, activity, age, sex), ...])
    No other text should be produced!"""
