import os

def getAllFiles_in_run():
    # Specify the directory where you want to start the search
    directory_path = "Chat_GPT_Generated_Code/Run_5/"

    # Use os.walk to traverse through the directory and its subdirectories
    python_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.startswith("mutation"):
                python_files.append(os.path.join(root, file))

    return python_files

print(getAllFiles_in_run())
