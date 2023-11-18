import re
import os
import shutil

def extractPythonCode(lines):
    modified_lines = []
    inside_code_block = False

    for line in lines:
        if line.strip().startswith("def "):
            inside_code_block = True
        if inside_code_block:
            if not(line.startswith((' ', '\t', 'def'))):
                modified_lines.append("#" + line)
            else:
                modified_lines.append(line)
        else:
            if(line.startswith('import')):
                modified_lines.append(line)
            else:
                modified_lines.append("#" + line)

    modified_code = '\n'.join(modified_lines)

    return modified_code



def filesGenerator(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        exit()

    with open(file_path, 'r') as file:
        file_contents = file.read()

    section_headers = re.findall(r'#\d+ (.+\.py)', file_contents)
    sections = re.split(r'#\d+ .+\.py', file_contents)[1:]

    for i, (section_header, section_content) in enumerate(zip(section_headers, sections), 1):
        section_name = section_header.strip().replace('\\', '_').replace('/', '_').replace(' ', '_')
        filename = f'{section_name}'

        pattern = r'(.*?)\.py'

        # Use re.search to find the pattern in the input string
        match_filename = re.search(pattern, filename)

        # Check if a match was found
        if match_filename:
            extracted_filename = match_filename.group(1)  # Extract the text between "python_programs" and ".py"
            filename = extracted_filename
            print(filename)
        else:
            print("Pattern not found in the input string.")
        parts = section_header.split('\\')

        extracted_string = parts[-1]

        lines = section_content.split('\n')

        modified_code = extractPythonCode(lines)

        target_folder_name = "QuixBugs/gptTOcodeNonCommented/"
        # Ensure the 'disjoint' directory exists or create it
        os.makedirs(target_folder_name, exist_ok=True)

        # Create the full path for the new Python file with .py extension
        new_filename = f"{filename}.py"
        new_filepath = os.path.join(target_folder_name, new_filename)

        # Open the new Python file in write ('w') mode and write content
        with open(new_filepath, 'w') as newfile:
            newfile.write("#" + extracted_string + '\n' + modified_code.strip())

    print(f'{len(section_headers)} sections extracted and saved to separate Python files in the gptToCode folder.')




file_path = "Quixbugs/Run-10-quixbugs-non-commented.txt"

filesGenerator(file_path)