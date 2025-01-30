import json

def save_results_as_json(out_raw_prompt, out_prompt, output_raw, output, output_path):
    '''
        Save the results as a JSON file.

        Args:
            out_raw_prompt (str): Prompt for LLaVA.
            out_prompt (str): Prompt for Gemini.
            output_raw (str): Persons information.
            output (dict): Persons information formatted.
            output_path (str): Path to save the JSON file.
    '''

    data = {
        "llava_prompt": out_raw_prompt,
        "gemini_prompt": out_prompt,
        "output_raw": output_raw,
        "output": output
    }

    with open(output_path, "w") as file:
        json.dump(data, file, indent=4)