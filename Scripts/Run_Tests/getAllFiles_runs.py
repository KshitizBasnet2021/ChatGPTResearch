import os
import re


def getAllFiles_in_run():
    # Specify the directory where you want to start the search
    directory_path = "Chat_GPT_Generated_Code/Mutation_Run/"

    # Use os.walk to traverse through the directory and its subdirectories
    python_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.startswith("mutation"):
                python_files.append(os.path.join(root, file))

    return python_files
x = getAllFiles_in_run()
for filez in x:
    pattern = r'mutation_(\S+)'
    # Use re.search to find the first match
    match = re.search(pattern, filez)
    # Create the full path for the new Python file with .py extension
    new_filename = match.group(0)
    print(new_filename)