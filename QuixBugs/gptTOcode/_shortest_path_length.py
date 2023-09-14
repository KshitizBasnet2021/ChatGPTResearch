#../python_programs/shortest_path_length.py
#
#Yes, there is a bug in the provided code. In the `get` function, the default return value is incorrect. It should return `float('inf')` instead of `0` when the wanted node is not found in the node heap.
#
#Here is the corrected code:
#
#```python
def get(node_heap, wanted_node):
    for dist, node in node_heap:
        if node == wanted_node:
            return dist
    return float('inf')
#```
#
#Other than that, the code looks fine.
#
#
#