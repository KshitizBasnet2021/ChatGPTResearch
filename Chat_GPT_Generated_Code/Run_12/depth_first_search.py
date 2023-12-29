#depth_first_search.py
#
#There is a bug in the provided code. The bug is in the line `elif node is goalnode:`. The `is` operator checks for object identity, not equality. So, this line will only return True if `node` and `goalnode` are the exact same object, not if they have the same value.
#
#To fix this bug, you should use the `==` operator instead of `is` to check for equality. The corrected line should be `elif node == goalnode:`.
#
#Here is the corrected code:
#
def depth_first_search(startnode, goalnode):
    nodesvisited = set()
#
    def search_from(node):
        if node in nodesvisited:
            return False
        elif node == goalnode:
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