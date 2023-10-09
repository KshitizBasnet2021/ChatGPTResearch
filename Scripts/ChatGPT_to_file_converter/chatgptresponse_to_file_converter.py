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



def filesGenerator(file_path, chapter_no,run):
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
        filename = f'{section_name}.py'
        parts = section_header.split('\\')
        extracted_string = parts[-1]

        lines = section_content.split('\n')

        modified_code = extractPythonCode(lines)

        disjoint = f'Chat_GPT_Generated_Code/Run_{run}/ch{chapter_no}/'+parts[-2]
        mutation_number = i

        # Ensure the 'disjoint' directory exists or create it
        os.makedirs(disjoint, exist_ok=True)

        # Create the full path for the new Python file with .py extension
        # new_filename = f"mutation_{mutation_number}.py"
        new_filename = re.search(r'_obs_(.*?)\.py', filename).group(1)
    
        pattern = r'def\s+(\w+)\('  # This pattern captures the function name
        modified_code = re.sub(pattern, f'def {new_filename}(', modified_code)

        new_filename = new_filename + ".py"
        new_filepath = os.path.join(disjoint, new_filename)
        
        # Open the new Python file in write ('w') mode and write content
        with open(new_filepath, 'w') as newfile:
            newfile.write("#" + extracted_string + '\n' + modified_code.strip())

    print(f'{len(section_headers)} sections extracted and saved to separate Python files in the  folder.')


# run = 5
# chapters = ['03', '04', '05', '10', '12', '13']
# for chapter in chapters:
#     file_path = f'{os.getcwd()}/Runs/Run_5_Commented_Code/Run-5-ch{chapter}-chatgpt-response-for-obs-commented.txt'
#     # file_path = f'Runs/Run_1_commented_code/run-1_ch{chapter}_commented_code.txt'
#     filesGenerator(file_path, chapter,run)

file_path = f'{os.getcwd()}/Runs/Run-6-quixbox-chatgpt-response-for-obs-commented.txt'
filesGenerator(file_path, 0,6)

