import os
import re

def extract_number(line):
    pattern = r'^\+\s+(\d+):'
    match = re.match(pattern, line)
    
    if match:
        number = match.group(1)
        return number
    else:
        return None

def generate_mutation_files(report_file, code_file, folder):
    with open(report_file, 'r') as report:
        report_lines = report.readlines()

    mutations = []
    pattern = r'^\+\s+\d+:'
    for line in report_lines:
        if re.match(pattern, line):
            mutations.append(line)

    with open(code_file, 'r') as code:
        code_content = code.read()

    for i, mutation in enumerate(mutations, start=1):
        mutation_content = mutation.strip()
        mutation_filename = f'mutation_{i}.py'
        filepath = os.path.join(folder, mutation_filename)
       # print("Adding Files to" + filepath)
        with open(filepath, 'w') as mutation_file:
            con = code_content + '\n' + mutation_content
            # Split the text into lines
            lines = con.split('\n')
            # get the last line
            last_line = lines[-1]
            # Insert last line in the line where it deserves and remove the unnecessary code
            getNumberLine = extract_number(last_line)
            lines[(int(getNumberLine))-1] = last_line
            # Join the lines back together but remove the last line
            modified_text = '\n'.join(lines[:-1])
            mutation_file.write(modified_text)



if __name__ == "__main__":
    mutation_report_file1 = './Tests_No_Comments/ch12/MutationsCh12/mutation_merge_array.txt'
    code_file1 = './ch12/No_Comments/merge_array.py'
    dir_path1 = './Tests_No_Comments/Ch12/MutationsCh12/merge_array'


    generate_mutation_files(mutation_report_file1, code_file1, dir_path1)


