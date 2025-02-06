IMAGE_NAME = "IMG_3032"
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

LLAVA_PROMPT = """Analyze the given image and provide a description for each person present. For each person, output the following attributes:

Activity: Choose from the following predefined categories:
Cuddling, standing alone, standing together, reading, sleeping, eating/drinking, playing alone, playing together, conversation, walking alone, walking in a group, playing with a pet.

Sex: Male or female. If uncertain, make the best guess based on visible features such as clothing, hairstyle, or posture.

Age range: Choose from "child," "adult," or "senior." If uncertain, make an informed guess based on body proportions, posture, and apparent physical features.

If a person is partially visible or obscured, use contextual clues to infer the missing details. Even when the certainty is low, provide the best possible guess rather than leaving attributes undefined.
Ensure that all people in the image are included in the response.
"""

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