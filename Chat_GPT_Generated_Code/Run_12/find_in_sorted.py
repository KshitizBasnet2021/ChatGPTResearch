#find_in_sorted.py
#
#The code provided seems to have a bug in the recursive call to `binsearch` when `x < arr[mid]`. The start index for the next recursive call should be `start` instead of `start + 1`. 
#
#Here's the corrected code:
#
#```python
def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid + 1, end)
        else:
            return mid
#
    return binsearch(0, len(arr))
#```
#
#With this fix, the code should work correctly to find the index of `x` in the sorted array `arr`.
#
#
#