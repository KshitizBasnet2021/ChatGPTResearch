
"""
lIIIIllIllIlI

Input:
    llIIlIIIIlIllIllI: A positive int representing an upper bound.

Output:
    A list containing all primes up to and including llIIlIIIIlIllIllI
"""

def lIIIIllIllIlI(llIIlIIIIlIllIllI):
    IlllllIlIIIII = []
    for lIIIlIllll in range(2, llIIlIIIIlIllIllI + 1):
        if any(lIIIlIllll % IlIIlIII > 0 for IlIIlIII in IlllllIlIIIII):
            IlllllIlIIIII.append(lIIIlIllll)
    return IlllllIlIIIII