#kheapsort.py
#
#There is a bug in the provided code. The bug is in the line `for x in arr:`. This line should iterate over the elements of `arr[k:]` instead of `arr`. 
#
#Here is the corrected code:
#
#```python
def kheapsort(arr, k):
    import heapq
#
    heap = arr[:k]
    heapq.heapify(heap)
#
    for x in arr[k:]:
        yield heapq.heappushpop(heap, x)
#
    while heap:
        yield heapq.heappop(heap)
#```
#
#This code will correctly perform k-way heapsort on the input array.
#
#
#