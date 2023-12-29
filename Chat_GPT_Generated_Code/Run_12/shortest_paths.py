#shortest_paths.py
#
#Yes, there is a bug in the provided code. The bug is in the inner loop where the weights are updated. The code is currently updating the weight of node v with the minimum of the current weight of node v and the sum of the weight of node u and the weight of the edge (u, v). However, this is incorrect because it should be updating the weight of node v with the minimum of the current weight of node v and the sum of the weight of node u and the weight of the edge (u, v) only if the sum is smaller than the current weight of node v.
#
#Here is the corrected code:
#
def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0
#
    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            if weight_by_node[u] + weight < weight_by_node[v]:
                weight_by_node[v] = weight_by_node[u] + weight
#
    return weight_by_node
#
#
#