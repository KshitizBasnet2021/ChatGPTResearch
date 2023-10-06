#mutation_12_line_no_6_ROR.py
#
#There is a bug in the provided code. The variable names are not clear and do not follow the Python naming conventions. Additionally, the code is not properly indented.
#
#Here's the fixed code with improved variable names and proper indentation:
#
def find_substring(main_string, substring):
    main_length, sub_length = len(main_string), len(substring)
    
    for i in range(main_length - sub_length + 1):
        j = 0
        while j < sub_length and main_string[i + j] == substring[j]:
            j += 1
        if j == sub_length:
            return i
    return -1
#
#Now the code is more readable and follows the Python naming conventions.
#
#
#