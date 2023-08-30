import os
import re
import shutil

pattern_line_change = r'^\+\s+(\d+):'
pattern_mutation_name = r"\[#\s+\d+\]\s+(.+):"

def extract_number(line):
    
    match_line_change = re.match(pattern_line_change, line)
    
    if match_line_change:
        number = match_line_change.group(1)
        return number
    else:
        return None
    
def align_and_replace(text1, text2):
    # Extract the relevant part of Text 1 by removing the prefix "+ 29:" and whitespace
    text1_cleaned = text1[text1.index(":") + 1:].strip()

    # Find the indentation of Text 2
    indentation = len(text2) - len(text2.lstrip())

    # Create the aligned text by combining the indentation and cleaned Text 1
    aligned_text = " " * indentation + text1_cleaned

    # Combine Text 2 and a comment with original Text 1 content on the same line
    replaced_text = aligned_text  # + "  # " + text2

    return replaced_text

def generate_mutation_files(report_file, code_file, folder):
    with open(report_file, 'r') as report:
        report_lines = report.readlines()

    mutations = []
    mutations_name = []
    for line in report_lines:
        if re.match(pattern_line_change, line):
            mutations.append(line)

        match = re.search(pattern_mutation_name, line)

        if match:
            aor_part = match.group(1)
            mutations_name.append(aor_part[0:3])  
    
    with open(code_file, 'r') as code:
        code_content = code.read()

    for i, mutation in enumerate(mutations, start=1):
        mutation_content = mutation.strip()
        mutation_filename = f'mutation_{i}_.py'
        filepath = os.path.join(folder, mutation_filename)

        linenum = 0
        with open(filepath, 'w') as mutation_file:
            con = code_content + '\n' + mutation_content
            # Split the text into lines
            lines = con.split('\n')
            # get the last line
            last_line = lines[-1]
            # Insert last line in the line where it deserves and remove the unnecessary code
            getNumberLine = extract_number(last_line)
            linenum = getNumberLine
            lines[(int(linenum))-1] = align_and_replace(last_line,lines[(int(getNumberLine))-1])
            # Join the lines back together but remove the last line
            modified_text = '\n'.join(lines[:-1])
            mutation_file.write(modified_text)
        
        # Rename the file to the desired new filename
        mutation_name = mutations_name[i-1]
        new_mutation_filename = f'mutation_{i}_line_no_{linenum}_{mutation_name[0:3]}.py'
        new_filepath = os.path.join(folder, new_mutation_filename)
        shutil.move(filepath, new_filepath)
            



if __name__ == "__main__":
    # mutation_report_file1 = './Tests_Final/ch03/Mutation/Commented_Code/disjoint/mutation_disjoint.txt'
    # code_file1 = './ch03/disjoint.py'
    # dir_path1 = './Tests_Final/Ch03/Mutation/Commented_Code/disjoint'

    mutation_report_file1 = './Tests_Final/ch03/Mutation/Non_Commented_Code/disjoint/mutation_disjoint.txt'
    code_file1 = './ch03/No_Comments/disjoint.py'
    dir_path1 = './Tests_Final/Ch03/Mutation/Non_Commented_Code/disjoint'



    generate_mutation_files(mutation_report_file1, code_file1, dir_path1)


