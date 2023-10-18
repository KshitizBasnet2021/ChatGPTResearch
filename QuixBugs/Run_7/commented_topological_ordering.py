#topological_ordering.py
#
#Yes, there is a bug in the provided code. The bug is in the line `if set(lIIllIIlI).issuperset(llllllllIllllIlIII.outgoing_nodes) and llllllllIllllIlIII not in lIIllIIlI:`. 
#
#The bug is that the condition `set(lIIllIIlI).issuperset(llllllllIllllIlIII.outgoing_nodes)` is checking if the set of nodes in `lIIllIIlI` is a superset of the outgoing nodes of `llllllllIllllIlIII`. However, it should be checking if the set of nodes in `lIIllIIlI` is a subset of the incoming nodes of `llllllllIllllIlIII`. 
#
#To fix the bug, we need to change the condition to `set(llllllllIllllIlIII.incoming_nodes).issuperset(lIIllIIlI)`.
#
#Here's the corrected code:
#
#"""
#Topological Sort
#
#Input:
#    nodes: A list of directed graph nodes
#
#Precondition:
#    The input graph is acyclic
#
#Output:
#    An OrderedSet containing the elements of nodes in an order that puts each node before all the nodes it has edges to
#"""
#
def topological_ordering(llIIllIllIl):
    lIIllIIlI = [IlllIIIIllIIllI for IlllIIIIllIIllI in llIIllIllIl if not IlllIIIIllIIllI.incoming_nodes]
    for IlllIIIIllIIllI in lIIllIIlI:
        for llllllllIllllIlIII in IlllIIIIllIIllI.outgoing_nodes:
            if set(llllllllIllllIlIII.incoming_nodes).issuperset(lIIllIIlI) and llllllllIllllIlIII not in lIIllIIlI:
                lIIllIIlI.append(llllllllIllllIlIII)
    return lIIllIIlI
#
#
#