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
    mutation_report_file1 = './Tests_No_Comments/ch04/MutationsCh04/mutation_binary_search_iterative.txt'
    code_file1 = './ch04/No_Comments/binary_search_iterative.py'
    dir_path1 = './Tests_No_Comments/Ch04/MutationsCh04/Binary_Search_iterative'

    mutation_report_file2 = './Tests_No_Comments/ch04/MutationsCh04/mutation_binary_sum.txt'
    code_file2 = './ch04/No_Comments/binary_sum.py'
    dir_path2 = './Tests_No_Comments/Ch04/MutationsCh04/binary_sum'

    
    mutation_report_file3 = './Tests_No_Comments/ch04/MutationsCh04/mutation_power_fast.txt'
    code_file3 = './ch04/No_Comments/power_fast.py'
    dir_path3 = './Tests_No_Comments/Ch04/MutationsCh04/power_fast'

    mutation_report_file4 = './Tests_No_Comments/ch04/MutationsCh04/mutation_reverse.txt'
    code_file4 = './ch04/No_Comments/reverse.py'
    dir_path4 = './Tests_No_Comments/Ch04/MutationsCh04/reverse'

    mutation_report_file5 = './Tests_No_Comments/ch04/MutationsCh04/mutation_reverse_iterative.txt'
    code_file5 = './ch04/No_Comments/reverse_iterative.py'
    dir_path5 = './Tests_No_Comments/Ch04/MutationsCh04/reverse_iterative'

    generate_mutation_files(mutation_report_file1, code_file1, dir_path1)
    generate_mutation_files(mutation_report_file2, code_file2, dir_path2)
    generate_mutation_files(mutation_report_file3, code_file3, dir_path3)
    generate_mutation_files(mutation_report_file4, code_file4, dir_path4)
    generate_mutation_files(mutation_report_file5, code_file5, dir_path5)

