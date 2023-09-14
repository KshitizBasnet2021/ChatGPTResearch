#../python_programs/find_first_in_sorted.py
#
#Yes, there is a bug in the provided code. The bug is in the line `hi = len(arr)`. The variable `hi` should be initialized to `len(arr) - 1` instead of `len(arr)`. This is because the index of the last element in the array is `len(arr) - 1`, not `len(arr)`.
#
#Here is the corrected code:
#
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
#
#Now the code should work correctly.
#
#
#