
"""
IllIllIIlIIllIIIll


Kruskal's algorithm implementation.

Input:
    lIIIlIIIIlllIl: A dict of the form {(u, v): weight} for every undirected graph edge {u, v}

Precondition:
    The input graph is connected

Output:
    A set of edges that connects all the vertices of the input graph and has the least possible total weight.

Example:
    # >>> IllIllIIlIIllIIIll({
    # ...     (1, 2): 10,
    # ...     (2, 3): 15,
    # ...     (3, 4): 10,
    # ...     (1, 4): 10
    # ... })
    {(1, 2), (3, 4), (1, 4)}
"""

def IllIllIIlIIllIIIll(lIIIlIIIIlllIl):
    lIIIlIIIlllIIIlII = {}
    IIIIIllIIIIIlII = set()
    for llllIIIIIIll in sorted(lIIIlIIIIlllIl, key=lIIIlIIIIlllIl.__getitem__):
        IlllIlllll, lIIlIIll = llllIIIIIIll
        if lIIIlIIIlllIIIlII.setdefault(IlllIlllll, {IlllIlllll}) != lIIIlIIIlllIIIlII.setdefault(lIIlIIll, {lIIlIIll}):
            IIIIIllIIIIIlII.add(llllIIIIIIll)
            lIIIlIIIlllIIIlII[IlllIlllll].update(lIIIlIIIlllIIIlII[lIIlIIll])
            for IlIIIllllIIllllll in lIIIlIIIlllIIIlII[lIIlIIll]:
                lIIIlIIIlllIIIlII[IlIIIllllIIllllll].update(lIIIlIIIlllIIIlII[IlllIlllll])
    return IIIIIllIIIIIlII