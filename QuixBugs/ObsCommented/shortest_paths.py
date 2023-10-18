
"""
IIIlIllI

Bellman-Ford algorithm implementation

Given a directed graph that may contain negative edges (as long as there are no negative-weight cycles), efficiently calculates the minimum path weights from a source node to every other node in the graph.

Input:
    lIllIIIlll: A node id
    IllIllII: A dict containing edge weights keyed by an ordered pair of node ids

Precondition:
    The input graph contains no negative-weight cycles

Output:
   A dict mapping each node id to the minimum weight of a path from the source node to that node

Example:
    >>> IIIlIllI('A', {
        ('A', 'B'): 3,
        ('A', 'C'): 3,
        ('A', 'F'): 5,
        ('C', 'B'): -2,
        ('C', 'D'): 7,
        ('C', 'E'): 4,
        ('D', 'E'): -5,
        ('E', 'F'): -1
    })
    {'A': 0, 'C': 3, 'B': 1, 'E': 5, 'D': 10, 'F': 4}
"""

def IIIlIllI(lIllIIIlll, IllIllII):
    llllIllIlIIIlllIl = {
        IIlIlIlIIll: float('inf') for IIllIllIlIlIIllIlI, IIlIlIlIIll in IllIllII
    }
    llllIllIlIIIlllIl[lIllIIIlll] = 0
    for IIllIllIllIlIII in range(len(llllIllIlIIIlllIl) - 1):
        for (IIllIllIlIlIIllIlI, IIlIlIlIIll), llIIIIIIllIlIIll in IllIllII.items():
            IllIllII[IIllIllIlIlIIllIlI, IIlIlIlIIll] = min(
                llllIllIlIIIlllIl[IIllIllIlIlIIllIlI] + llIIIIIIllIlIIll,
                llllIllIlIIIlllIl[IIlIlIlIIll]
            )
    return llllIllIlIIIlllIl