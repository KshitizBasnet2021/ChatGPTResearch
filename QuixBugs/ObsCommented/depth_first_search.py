
"""
IlIIlIIIl


Input:
    IIIlIlIlllIl: A digraph node
    IIIlIIlllIlIl: A digraph node

Output:
    Whether IIIlIIlllIlIl is reachable from IIIlIlIlllIl
"""

def IlIIlIIIl(IIIlIlIlllIl, IIIlIIlllIlIl):
    IlIIllllll = set()
    def search_from(llIlIlIIlllIII):
        if llIlIlIIlllIII in IlIIllllll:
            return False
        elif llIlIlIIlllIII is IIIlIIlllIlIl:
            return True
        else:
            return any(
                search_from(IIIllIlIIIlIIIl) for IIIllIlIIIlIIIl in llIlIlIIlllIII.successors
            )
    return search_from(IIIlIlIlllIl)