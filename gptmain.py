import time
import openai
import os

from getAllFiles import getPythonFiles

# Your OpenAI API key
api_key = "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"

# Function to check if a Python code file is buggy
def is_code_buggy(file_path):
    # Implement your logic to check if the code is buggy here
    # You can use static analysis tools or test the code, for example
    # For simplicity, let's assume all code is buggy
    return True

# Function to interact with ChatGPT and correct code if it's buggy
def chat_with_gpt(code, filename, count):
    openai.api_key = api_key
    prompt = (
        f"Please provide information about the bug in the code in the following format:"
         "Bug: [Yes or No]"
         "Description: (limit to 20 words)"
         "Code Snippet: [Corrected Code]\n\n"
        f"the code is: {code}\n\n"
    )

    # Make the API request
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
    )
    time.sleep(3)
    # Extract and return the generated text
    generated_text = response.choices[0].text.strip()
    print(generated_text)
    return "#"+str(count)+" "+filename+'\n'+ generated_text +"\n"

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
