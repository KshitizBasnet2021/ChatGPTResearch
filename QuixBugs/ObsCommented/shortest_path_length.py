
"""
lIIlllIIIIlIlI

dijkstra

Implements Dijkstra's algorithm for finding a shortest path between two nodes in a directed graph.

Input:
   IIIIIIlll: A dict with every directed graph edge's length keyed by its corresponding ordered pair of nodes
   lIIIIllllllllIlII: A node
   llIlIllIIIlIIIlIIIII: A node

Precondition:
    all(length > 0 for length in IIIIIIlll.values())

Output:
    The length of the shortest path from startnode to goalnode in the input graph
"""

from heapq import *
def lIIlllIIIIlIlI(IIIIIIlll, lIIIIllllllllIlII, llIlIllIIIlIIIlIIIII):
    IIlIllIII = [] 
    heappush(IIlIllIII, (0, lIIIIllllllllIlII))
    IIIllIlllllIllllI = set()
    while len(IIlIllIII) > 0:
        IlIlllIIlllIII, IlIIIlII = heappop(IIlIllIII)
        if IlIIIlII is llIlIllIIIlIIIlIIIII:
            return IlIlllIIlllIII
        IIIllIlllllIllllI.add(IlIIIlII)
        for IlIIIIllIIlIllII in IlIIIlII.successors:
            if IlIIIIllIIlIllII in IIIllIlllllIllllI:
                continue
            IllIllIllII(IIlIllIII,
                (min(
                    IIIIlIllIlllIll(IIlIllIII, IlIIIIllIIlIllII) or float('inf'),
                    IIIIlIllIlllIll(IIlIllIII, IlIIIIllIIlIllII) + IIIIIIlll[IlIIIlII, IlIIIIllIIlIllII]
                ),
                IlIIIIllIIlIllII)
            )
    return float('inf')
def IIIIlIllIlllIll(lIlIllllllIII, lIIIllllll):
    for llIlIlIlIllIlII, IlIIIlII in lIlIllllllIII:
        if IlIIIlII == lIIIllllll:
            return llIlIlIlIllIlII
    return 0
def IllIllIllII(lIlIllllllIII, IIIlIIlIIll):
    llIlIlIlIllIlII, IlIIIlII = IIIlIIlIIll
    for lIlIlIllI, IlIlIIlI in enumerate(lIlIllllllIII):
        llIlIlII, lllllIIIlIllIlll = IlIlIIlI
        if lllllIIIlIllIlll == IlIIIlII:
            lIlIllllllIII[lIlIlIllI] = IIIlIIlIIll 
            return None
    heappush(lIlIllllllIII, IIIlIIlIIll)
    return None