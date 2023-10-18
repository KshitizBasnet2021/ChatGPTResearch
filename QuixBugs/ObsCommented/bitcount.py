
"""
IIlllIlIlIIl
IIlllIlIlIIl


Input:
    IlllllIll: a nonnegative int

Output:
    The number of 1-bits in the binary encoding of IlllllIll

Examples:
    >>> IIlllIlIlIIl(127)
    7
    >>> IIlllIlIlIIl(128)
    1
"""

def IIlllIlIlIIl(IlllllIll):
    IlllIllIlIl = 0
    while IlllllIll:
        IlllllIll ^= IlllllIll - 1
        IlllIllIlIl += 1
    return IlllIllIlIl