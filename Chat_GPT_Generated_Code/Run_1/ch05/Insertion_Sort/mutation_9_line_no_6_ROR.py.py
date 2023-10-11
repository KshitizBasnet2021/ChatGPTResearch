#mutation_9_line_no_6_ROR.py
#
#The provided code is missing proper indentation. Here is the corrected code:
#
def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):         # from 1 to n-1
        cur = A[k]                       # current element to be inserted
        j = k                            # find correct index j for current
        while (j > 0 and A[j - 1] >= cur):
            A[j] = A[j-1]
            j -= 1
        A[j] = cur                       # cur is now in the right place
#
#The code itself looks correct and should work as intended. It implements the insertion sort algorithm to sort a list of comparable elements in non-decreasing order.
#
#
#