import json
import time
import openai
import os
import requests

from getAllFiles import getPythonFiles

# Your OpenAI API key
api_endpoint = "https://api.openai.com/v1/chat/completions"
api_key = "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"

# Function to check if a Python code file is buggy
def is_code_buggy(file_path):
    return True

# Function to interact with ChatGPT and correct code if it's buggy
def chat_with_gpt(code, filename, count):


# Define the prompt you want to send to the model
    prompt = (
        "Hi ChatGPt, "
        f"Provided Code: {code}\n\n"
        f"Do you see any bugs in the provided code, if so, can you fix it. \n"
        # Your response should be in the following format:
        #  "Bug: [Yes or No]\n"
        #  "Description: [Describe the bug but limit it to 20 words]\n"
        #  "Code Snippet: [Full Corrected Code]"
    )

# Define the parameters for the API request
    params = {
        "model": "gpt-3.5-turbo",  # This is the ChatGPT model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

# Define the headers, including your API key
    headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
    }

# Make the API request
    response = requests.post(api_endpoint, json=params, headers=headers)

    # Parse and print the response
    if response.status_code == 200:
        result = json.loads(response.text)
        return "#"+str(count)+" "+filename+'\n'+ result["choices"][0]["message"]["content"] +"\n" 
    else:
        print("Error:", response.status_code, response.text)
        
       

# List of Python file locations
python_files = getPythonFiles()

# Create a text file to store the responses
output_file = "responses.txt"

# Iterate over the Python files
with open(output_file, "w") as output_file:
    count = 0
    for file_path in python_files:
        with open(file_path, "r") as python_file:
            code = python_file.read()
            count = count + 1
            corrected_code = chat_with_gpt(code, file_path, count)
            output_file.write(corrected_code + "\n\n")

print(f"Responses saved in {output_file}")
