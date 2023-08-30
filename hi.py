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

    # mutation_report_file1 = './Tests_Final/ch03/Mutation/Non_Commented_Code/disjoint/mutation_disjoint.txt'
    # code_file1 = './ch03/No_Comments/disjoint.py'
    # dir_path1 = './Tests_Final/Ch03/Mutation/Non_Commented_Code/disjoint'

    # mutation_report_file1 = './Tests_Final/ch03/Mutation/Commented_Code/find/mutation_find.txt'
    # code_file1 = './ch03/find.py'
    # dir_path1 = './Tests_Final/Ch03/Mutation/Commented_Code/find'

    # mutation_report_file2 = './Tests_Final/ch03/Mutation/Non_Commented_Code/find/mutation_find.txt'
    # code_file2 = './ch03/No_Comments/find.py'
    # dir_path2 = './Tests_Final/Ch03/Mutation/Non_Commented_Code/find'

   
    # mutation_report_file3 = './Tests_Final/ch03/Mutation/Commented_Code/find_max/mutation_find_max.txt'
    # code_file3 = './ch03/find_max.py'
    # dir_path3 = './Tests_Final/Ch03/Mutation/Commented_Code/find_max'

    # mutation_report_file4 = './Tests_Final/ch03/Mutation/Non_Commented_Code/find_max/mutation_find_max.txt'
    # code_file4 = './ch03/No_Comments/find_max.py'
    # dir_path4 = './Tests_Final/Ch03/Mutation/Non_Commented_Code/find_max'

    # mutation_report_file5 = './Tests_Final/ch03/Mutation/Commented_Code/prefix_averages/mutation_prefix_averages.txt'
    # code_file5 = './ch03/prefix_averages.py'
    # dir_path5 = './Tests_Final/Ch03/Mutation/Commented_Code/prefix_averages'
   

    # mutation_report_file6 = './Tests_Final/ch03/Mutation/Non_Commented_Code/prefix_averages/mutation_prefix_averages.txt'
    # code_file6 = './ch03/No_Comments/prefix_averages.py'
    # dir_path6 = './Tests_Final/Ch03/Mutation/Non_Commented_Code/prefix_averages'

   
    # mutation_report_file7 = './Tests_Final/ch03/Mutation/Commented_Code/unique/mutation_unique.txt'
    # code_file7 = './ch03/unique.py'
    # dir_path7 = './Tests_Final/Ch03/Mutation/Commented_Code/unique'

    # mutation_report_file8 = './Tests_Final/ch03/Mutation/Non_Commented_Code/unique/mutation_unique.txt'
    # code_file8 = './ch03/No_Comments/unique.py'
    # dir_path8 = './Tests_Final/Ch03/Mutation/Non_Commented_Code/unique'

    # mutation_report_file9 = './Tests_Final/ch04/Mutation/Commented_Code/Binary_Search_iterative/mutation__binary_search_iterative.txt'
    # code_file9 = './ch04/binary_search_iterative.py'
    # dir_path9 = './Tests_Final/Ch04/Mutation/Commented_Code/binary_search_iterative'

    # mutation_report_file10 = './Tests_Final/ch04/Mutation/Non_Commented_Code/Binary_Search_iterative/mutation_binary_search_iterative.txt'
    # code_file10 = './ch04/No_Comments/binary_search_iterative.py'
    # dir_path10 = './Tests_Final/Ch04/Mutation/Non_Commented_Code/binary_search_iterative'

    # mutation_report_file11 = './Tests_Final/ch04/Mutation/Commented_Code/binary_search/mutation__binary_search.txt'
    # code_file11 = './ch04/binary_search.py'
    # dir_path11 = './Tests_Final/Ch04/Mutation/Commented_Code/binary_search'

    # mutation_report_file12 = './Tests_Final/ch04/Mutation/Non_Commented_Code/binary_search/mutation_binary_search.txt'
    # code_file12 = './ch04/No_Comments/binary_search.py'
    # dir_path12 = './Tests_Final/Ch04/Mutation/Non_Commented_Code/binary_search'

    # mutation_report_file13 = './Tests_Final/ch04/Mutation/Commented_Code/binary_sum/mutation__binary_sum.txt'
    # code_file13 = './ch04/binary_sum.py'
    # dir_path13 = './Tests_Final/Ch04/Mutation/Commented_Code/binary_sum'

    # mutation_report_file14 = './Tests_Final/ch04/Mutation/Non_Commented_Code/binary_sum/mutation_binary_sum.txt'
    # code_file14 = './ch04/No_Comments/binary_sum.py'
    # dir_path14 = './Tests_Final/Ch04/Mutation/Non_Commented_Code/binary_sum'

    # mutation_report_file15 = './Tests_Final/ch04/Mutation/Commented_Code/disk_usage/mutation__disk_usage.txt'
    # code_file15 = './ch04/disk_usage.py'
    # dir_path15 = './Tests_Final/Ch04/Mutation/Commented_Code/disk_usage'

    # mutation_report_file16 = './Tests_Final/ch04/Mutation/Non_Commented_Code/disk_usage/mutation_disk_usage.txt'
    # code_file16 = './ch04/No_Comments/disk_usage.py'
    # dir_path16 = './Tests_Final/Ch04/Mutation/Non_Commented_Code/disk_usage'

    # mutation_report_file17 = './Tests_Final/ch04/Mutation/Commented_Code/power_fast/mutation__power_fast.txt'
    # code_file17 = './ch04/power_fast.py'
    # dir_path17 = './Tests_Final/Ch04/Mutation/Commented_Code/power_fast'

    # mutation_report_file18 = './Tests_Final/ch04/Mutation/Non_Commented_Code/power_fast/mutation_power_fast.txt'
    # code_file18 = './ch04/No_Comments/power_fast.py'
    # dir_path18 = './Tests_Final/Ch04/Mutation/Non_Commented_Code/power_fast'

    # mutation_report_file19 = './Tests_Final/ch04/Mutation/Commented_Code/reverse/mutation__reverse.txt'
    # code_file19 = './ch04/reverse.py'
    # dir_path19 = './Tests_Final/Ch04/Mutation/Commented_Code/reverse'

    # mutation_report_file20 = './Tests_Final/ch04/Mutation/Non_Commented_Code/reverse/mutation_reverse.txt'
    # code_file20 = './ch04/No_Comments/reverse.py'
    # dir_path20 = './Tests_Final/Ch04/Mutation/Non_Commented_Code/reverse'

    # mutation_report_file21 = './Tests_Final/ch04/Mutation/Commented_Code/reverse_iterative/mutation__reverse_iterative.txt'
    # code_file21 = './ch04/reverse_iterative.py'
    # dir_path21 = './Tests_Final/Ch04/Mutation/Commented_Code/reverse_iterative'

    # mutation_report_file22 = './Tests_Final/ch04/Mutation/Non_Commented_Code/reverse_iterative/mutation_reverse_iterative.txt'
    # code_file22 = './ch04/No_Comments/reverse_iterative.py'
    # dir_path22 = './Tests_Final/Ch04/Mutation/Non_Commented_Code/reverse_iterative'

    mutation_report_file23 = './Tests_Final/ch05/Mutation/Commented_Code/insertion_sort/mutation_insertion_sort.txt'
    code_file23 = './ch05/insertion_sort.py'
    dir_path23 = './Tests_Final/Ch05/Mutation/Commented_Code/insertion_sort'

    mutation_report_file24 = './Tests_Final/ch05/Mutation/Non_Commented_Code/insertion_sort/mutation_insertion_sort.txt'
    code_file24 = './ch05/No_Comments/insertion_sort.py'
    dir_path24 = './Tests_Final/Ch05/Mutation/Non_Commented_Code/insertion_sort'
   
    # generate_mutation_files(mutation_report_file1, code_file1, dir_path1)
    # generate_mutation_files(mutation_report_file2, code_file2, dir_path2)
    # generate_mutation_files(mutation_report_file3, code_file3, dir_path3)
    # generate_mutation_files(mutation_report_file4, code_file4, dir_path4)
    # generate_mutation_files(mutation_report_file5, code_file5, dir_path5)
    # generate_mutation_files(mutation_report_file6, code_file6, dir_path6)
    # generate_mutation_files(mutation_report_file7, code_file7, dir_path7)
    # generate_mutation_files(mutation_report_file8, code_file8, dir_path8)
    # generate_mutation_files(mutation_report_file9, code_file9, dir_path9)
    # generate_mutation_files(mutation_report_file10, code_file10, dir_path10)
    # generate_mutation_files(mutation_report_file11, code_file11, dir_path11)
    # generate_mutation_files(mutation_report_file12, code_file12, dir_path12)
    # generate_mutation_files(mutation_report_file13, code_file13, dir_path13)
    # generate_mutation_files(mutation_report_file14, code_file14, dir_path14)
    # generate_mutation_files(mutation_report_file15, code_file15, dir_path15)
    # generate_mutation_files(mutation_report_file16, code_file16, dir_path16)
    # generate_mutation_files(mutation_report_file17, code_file17, dir_path17)
    # generate_mutation_files(mutation_report_file18, code_file18, dir_path18)
    # generate_mutation_files(mutation_report_file19, code_file19, dir_path19)
    # generate_mutation_files(mutation_report_file20, code_file20, dir_path20)
    # generate_mutation_files(mutation_report_file21, code_file21, dir_path21)
    # generate_mutation_files(mutation_report_file22, code_file22, dir_path22)
    generate_mutation_files(mutation_report_file23, code_file23, dir_path23)
    generate_mutation_files(mutation_report_file24, code_file24, dir_path24)