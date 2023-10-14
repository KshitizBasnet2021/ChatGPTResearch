
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
    def IIIllllIIllI(llIlIlIIlllIII):
        if llIlIlIIlllIII in IlIIllllll:
            return False
        elif llIlIlIIlllIII is IIIlIIlllIlIl:
            return True
        else:
            return any(
                IIIllllIIllI(IIIllIlIIIlIIIl) for IIIllIlIIIlIIIl in llIlIlIIlllIII.successors
            )
    return IIIllllIIllI(IIIlIlIlllIl)