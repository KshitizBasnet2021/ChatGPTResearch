
"""
IIIllllIlIllIIII

Input:
    llIIllIllIl: A list of directed graph nodes

Precondition:
    The input graph is acyclic

Output:
    An OrderedSet containing the elements of nodes in an order that puts each node before all the nodes it has edges to
"""

def IIIllllIlIllIIII(llIIllIllIl):
    lIIllIIlI = [IlllIIIIllIIllI for IlllIIIIllIIllI in llIIllIllIl if not IlllIIIIllIIllI.incoming_nodes]
    for IlllIIIIllIIllI in lIIllIIlI:
        for llllllllIllllIlIII in IlllIIIIllIIllI.outgoing_nodes:
            if set(lIIllIIlI).issuperset(llllllllIllllIlIII.outgoing_nodes) and llllllllIllllIlIII not in lIIllIIlI:
                lIIllIIlI.append(llllllllIllllIlIII)
    return lIIllIIlI