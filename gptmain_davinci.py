
import openai
import os


from getAllFiles import getPythonFiles

# Your OpenAI API key
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to interact with ChatGPT and correct code if it's buggy
def chat_with_gpt(code, filename, count):


# Define the prompt you want to send to the model
    prompt = (
        f"Provided Code: {code}\n\n"
        f"Do you see any bugs in the provided code, if so, can you fix it. \n"
    )



    # Specify the model (text-davinci-003) and provide a prompt
    model = "text-davinci-003"

    # Make an API call to generate text
    response = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=500,  # Adjust the number of tokens based on your needs
    temperature =0
    )
    
    # Parse and print the response
    if response:
        # Extract and print the generated text
        generated_text = response.choices[0].text
        print(str(count)+" "+filename+" data written in the text file..")
        return "#"+str(count)+" "+filename+'\n'+ generated_text +"\n" 
    else:
        print("Error:")
        return "Eroor at " + filename 

# List of Python file locations
python_files = getPythonFiles()

# Create a text file to store the responses
output_directory = 'Runs/Run_4_Non_Commented_code/'

output_file = os.path.join(output_directory, 'run-4_ch13_non_commented_code.txt')
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
