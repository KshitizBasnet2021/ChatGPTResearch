#quicksort.py
#
#The provided code is missing the case when the elements in the array are equal to the pivot. To fix this, we can modify the code to include an additional condition in the list comprehensions to handle equal elements. Here's the updated code:
#
def quicksort(arr):
    if not arr:
        return []
#
    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    equal = [x for x in arr if x == pivot]
    greater = quicksort([x for x in arr[1:] if x > pivot])
    return lesser + equal + greater
#
#This modification ensures that elements equal to the pivot are included in the final sorted array.
#
#
#