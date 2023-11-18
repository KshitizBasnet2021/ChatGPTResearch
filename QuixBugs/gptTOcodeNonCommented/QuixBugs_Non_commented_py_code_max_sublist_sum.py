#max_sublist_sum.py
#
#The provided code has a bug. It does not handle cases where all elements in the array are negative. In such cases, the function should return the maximum negative element. 
#
#To fix this bug, we can initialize `max_ending_here` and `max_so_far` to negative infinity instead of zero. This way, even if all elements are negative, the function will return the maximum negative element. 
#
#Here's the updated code:
#
#```python
def max_sublist_sum(arr):
    max_ending_here = float('-inf')
    max_so_far = float('-inf')
#
    for x in arr:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
#
    return max_so_far
#```
#
#Now the function will correctly handle cases with all negative elements.
#
#
#