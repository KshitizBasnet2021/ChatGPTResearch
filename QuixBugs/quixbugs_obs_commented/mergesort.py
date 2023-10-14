
"""
IlllIIlIIlI


Input:
    IIIllIllIII: A list of ints

Output:
    The elements of IIIllIllIII in sorted order
"""

def IlllIIlIIlI(IIIllIllIII):
    def IIIllllIllIll(llllIllllIlIIl, IllIllIIIllIlIIl):
        lIIlIllIllII = []
        IlllIIIIllIIl = 0
        IIIlllIIIIl = 0
        while IlllIIIIllIIl < len(llllIllllIlIIl) and IIIlllIIIIl < len(IllIllIIIllIlIIl):
            if llllIllllIlIIl[IlllIIIIllIIl] <= IllIllIIIllIlIIl[IIIlllIIIIl]:
                lIIlIllIllII.append(llllIllllIlIIl[IlllIIIIllIIl])
                IlllIIIIllIIl += 1
            else:
                lIIlIllIllII.append(IllIllIIIllIlIIl[IIIlllIIIIl])
                IIIlllIIIIl += 1
        lIIlIllIllII.extend(llllIllllIlIIl[IlllIIIIllIIl:] or IllIllIIIllIlIIl[IIIlllIIIIl:])
        return lIIlIllIllII
    if len(IIIllIllIII) == 0:
        return IIIllIllIII
    else:
        lllIIIII = len(IIIllIllIII) // 2
        llllIllllIlIIl = IlllIIlIIlI(IIIllIllIII[:lllIIIII])
        IllIllIIIllIlIIl = IlllIIlIIlI(IIIllIllIII[lllIIIII:])
        return IIIllllIllIll(llllIllllIlIIl, IllIllIIIllIlIIl)