#find_first_in_sorted.py
#
#Yes, there is a bug in the provided code. The bug is in the line `hi = len(arr)` where the upper bound of the search range is set to the length of the array. This is incorrect because the upper bound should be `len(arr) - 1` since array indices start from 0.
#
#Here is the corrected code:
#
#```python
def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr) - 1
#
    while lo <= hi:
        mid = (lo + hi) // 2
#
        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid
#
        elif x <= arr[mid]:
            hi = mid - 1
#
        else:
            lo = mid + 1
#
    return -1
#```
#
#In the corrected code, the upper bound `hi` is set to `len(arr) - 1` and in the `elif` condition, `hi` is updated to `mid - 1` instead of `mid`.
#
#
#