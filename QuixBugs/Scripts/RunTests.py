import os
from pathlib import Path

def getPythonFiles():

    # Initialize an empty list to store file locations
    file_locations = []
    if True:
        quixbugs_root = Path(__file__).parent / ".."
    # Specify the path to the "Commented_Code" directory
        commented_code_path = f'{quixbugs_root}/python_programs/'

    # Check if the specified path exists
        if os.path.exists(commented_code_path):
            # Iterate through subdirectories and files in the directory
            for root, _, files in os.walk(commented_code_path):
                for file in files:
                    # Get the full path of the file
                    file_path = os.path.join(root, file)
                    #if file is a python file
                    if(file_path.endswith(".py")):
                        # Append the file location to the list
                        # print(file)
                        # print(file_path)
                        file_locations.append(file_path)

        else:
            print(f"The directory '{commented_code_path}' does not exist or is not a directory.")

    # Print the list of file locations
    # for location in file_locations:
    #  print(location)

    # print(len(file_locations))
    return file_locations

# Function to count words in a file
def count_words_in_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)

# List of file locations
file_locations = getPythonFiles()
# Initialize a variable to store the total word count
total_word_count = 0

# Loop through each file location in the list
for file_location in file_locations:
    word_count = count_words_in_file(file_location)
    total_word_count += word_count

print(getPythonFiles())

