#../python_programs/longest_common_subsequence.py
#
#The provided code is missing a base case for when both strings are empty. To fix this, we can add a condition at the beginning of the function to check if both strings are empty, and if so, return an empty string. Here's the updated code:
#
def longest_common_subsequence(a, b):
    if not a or not b:
        return ''
#
    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])
#
    else:
        return max(
            longest_common_subsequence(a, b[1:]),
            longest_common_subsequence(a[1:], b),
            key=len
        )
#
#
#