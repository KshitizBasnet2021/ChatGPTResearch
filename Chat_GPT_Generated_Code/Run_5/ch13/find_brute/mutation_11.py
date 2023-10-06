#mutation_11_line_no_6_ROR.py
#
#The provided code is a function that performs string matching using the brute force approach. It checks if a given pattern exists in a given text and returns the index of the first occurrence of the pattern in the text. If the pattern is not found, it returns -1.
#
#The code appears to be correct and does not contain any syntax errors. However, there is a minor issue with the variable names. It is recommended to use more descriptive variable names to improve code readability.
#
#Here is the updated code with improved variable names:
#
def string_matching(text, pattern):
  text_length, pattern_length = len(text), len(pattern)
  for i in range(text_length - pattern_length + 1):
    match_count = 0
    while (match_count <= pattern_length and text[i + match_count] == pattern[match_count]):
      match_count += 1
    if match_count == pattern_length:
      return i
  return -1
#
#The code should now be easier to understand and use.
#
#
#