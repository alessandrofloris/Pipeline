from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration, BitsAndBytesConfig
import torch
from config import config

def load_llava_model():
    '''
    Load the LLaVA model and processor.
    '''

    # Configure 4-bit quantization
    bnb_config = BitsAndBytesConfig(
        bnb_4bit_compute_dtype=torch.bfloat16 # Compute in bfloat16 for better precision (if your GPU supports it)
    )

    # Model and processor setup
    processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-vicuna-13b-hf")
    model = LlavaNextForConditionalGeneration.from_pretrained("llava-hf/llava-v1.6-vicuna-13b-hf", low_cpu_mem_usage=True, quantization_config=bnb_config)
    model.to("cuda:0")

    return model, processor

def generate_description(image, model, processor):
    """
        Generate a description of the image using LLaVA.

        Returns:
            description: A string describing the image.
    """

    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "text", "text": config.LLAVA_PROMPT}, 
            ],
        },
    ]

    prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
    inputs = processor(image, prompt, return_tensors="pt").to("cuda:0")
    output = model.generate(**inputs, max_new_tokens=1000)
    output = processor.decode(output[0], skip_special_tokens=True)

    assistant_output = output.split("ASSISTANT: ")[-1]
    
    return assistant_output

def generate_descriptions(images):
    """
        Generate a description of the images using LLaVA.

        Returns:
            descriptions: A list of strings describing the images.
    """

    model, processor = load_llava_model()

    descriptions = []

    for image in images:
        descriptions.append(generate_description(image, model, processor))

    return descriptions