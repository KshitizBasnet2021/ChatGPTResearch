
"""
IlIIlIllIl

Floyd-Warshall algorithm implementation.

Calculates the length of the shortest path connecting every ordered pair of nodes in a directed graph.



Input:
    lIIlIllIIllIIlll: The number of nodes in the graph. The nodes are assumed to have ids 0..n-1
    lIlIIllIlIlIlllllI: A dict containing edge length keyed by an ordered pair of node ids

Precondition:
    There are no negative-length cycles in the input graph

Output:
    A dict containing shortest path length keyed by an ordered pair of node ids
"""

from collections import defaultdict
def IlIIlIllIl(lIIlIllIIllIIlll, lIlIIllIlIlIlllllI):
    IllIIllll = defaultdict(lambda: float('inf'))
    IllIIllll.update({(IIlIIIIIlllIllIlII, IIlIIIIIlllIllIlII): 0 for IIlIIIIIlllIllIlII in range(lIIlIllIIllIIlll)})
    IllIIllll.update(lIlIIllIlIlIlllllI)
    for llllIllIIllIIlIllI in range(lIIlIllIIllIIlll):
        for IIlIIIIIlllIllIlII in range(lIIlIllIIllIIlll):
            for IllIlIllIllllIIlI in range(lIIlIllIIllIIlll):
                IllIIllll[IIlIIIIIlllIllIlII, IllIlIllIllllIIlI] = min(
                    IllIIllll[IIlIIIIIlllIllIlII, IllIlIllIllllIIlI],
                    IllIIllll[IIlIIIIIlllIllIlII, llllIllIIllIIlIllI] + IllIIllll[IllIlIllIllllIIlI, llllIllIIllIIlIllI]
                )
    return IllIIllll