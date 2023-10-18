
"""
llllIlIlI

Input:
    lIIIIlIIlIlllll: a string
    lllIIIIIIIIllIlI: a string

Output:
    Length of the longest substring common to lIIIIlIIlIlllll and lllIIIIIIIIllIlI

Example:
    >>> llllIlIlI('witch', 'sandwich')
    2
    >>> llllIlIlI('meow', 'homeowner')
    4
"""

def llllIlIlI(lIIIIlIIlIlllll, lllIIIIIIIIllIlI):
    from collections import Counter
    IlIIIlIlIIIlllIIIIll = Counter()
    for llllllIlIIlllllllI in range(len(lIIIIlIIlIlllll)):
        for lIIlllIllIIIl in range(len(lllIIIIIIIIllIlI)):
            if lIIIIlIIlIlllll[llllllIlIIlllllllI] == lllIIIIIIIIllIlI[lIIlllIllIIIl]:
                IlIIIlIlIIIlllIIIIll[llllllIlIIlllllllI, lIIlllIllIIIl] = IlIIIlIlIIIlllIIIIll[llllllIlIIlllllllI - 1, lIIlllIllIIIl] + 1
    return max(IlIIIlIlIIIlllIIIIll.values()) if IlIIIlIlIIIlllIIIIll else 0