#shortest_paths.py
#
#Yes, there is a bug in the provided code. The bug is in the inner loop where the weights are updated. The weights should be updated based on the minimum weight between the current weight and the sum of the weight from the source node to the current node and the weight of the current edge. However, in the code, the weights are updated based on the minimum weight between the weight from the source node to the current node and the weight of the current edge, and the weight of the current node.
#
#To fix this bug, we need to update the line:
#
#weight_by_edge[u, v] = min(
#    weight_by_node[u] + weight,
#    weight_by_node[v]
#)
#
#to:
#
#weight_by_node[v] = min(
#    weight_by_node[u] + weight,
#    weight_by_node[v]
#)
#
#Here's the corrected code:
#
def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0
#
    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            weight_by_node[v] = min(
                weight_by_node[u] + weight,
                weight_by_node[v]
            )
#
    return weight_by_node
#
#
#