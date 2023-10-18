
"""
IIlIlIIlIIIIlI

Efficient equivalent to max(sum(arr[i:j]) for 0 <= i <= j <= len(arr))

Algorithm source: WordAligned.org by Thomas Guest


Input:
    lIIlIIIlIllIlI: A list of ints

Output:
    The maximum sublist sum

Example:
    >>> IIlIlIIlIIIIlI([4, -5, 2, 1, -1, 3])
    5
"""

def IIlIlIIlIIIIlI(lIIlIIIlIllIlI):
    lIlllIIIIIlIIllI = 0
    IllIIIIlIllIIl = 0
    for IlIIllll in lIIlIIIlIllIlI:
        lIlllIIIIIlIIllI = lIlllIIIIIlIIllI + IlIIllll
        IllIIIIlIllIIl = max(IllIIIIlIllIIl, lIlllIIIIIlIIllI)
    return IllIIIIlIllIIl