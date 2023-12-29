#kheapsort.py
#
#The provided code is missing a closing parenthesis on the last line. Here is the corrected code:
#
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
#
#
#