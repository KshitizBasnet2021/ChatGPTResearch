#depth_first_search.py
#
#There is a bug in the provided code. The bug is that the `nodesvisited` set is not being updated with the nodes that have been visited. This can lead to an infinite loop if there is a cycle in the graph.
#
#To fix this bug, we need to update the `nodesvisited` set with the nodes that have been visited. We can do this by adding the `node` to the `nodesvisited` set before making the recursive call to `search_from(nextnode)`.
#
#Here is the updated code:
#
def depth_first_search(startnode, goalnode):
    nodesvisited = set()
#
    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            nodesvisited.add(node)
            return any(
                search_from(nextnode) for nextnode in node.successors
            )
#
    return search_from(startnode)
#
#
#