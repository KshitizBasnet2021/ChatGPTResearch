
"""
IIIlIlIlllIIllIIIll


Factors an int using naive trial division.

Input:
    IllIIlIlIIIIIl: An int to factor

Output:
    A list of the prime factors of IllIIlIlIIIIIl in sorted order with repetition

Precondition:
    IllIIlIlIIIIIl >= 1

Examples:
    >>> IIIlIlIlllIIllIIIll(1)
    []
    >>> IIIlIlIlllIIllIIIll(100)
    [2, 2, 5, 5]
    >>> IIIlIlIlllIIllIIIll(101)
    [101]
"""

def IIIlIlIlllIIllIIIll(IllIIlIlIIIIIl):
    if IllIIlIlIIIIIl == 1:
        return []
    for IlIIIIlIllIIIIIlIlll in range(2, int(IllIIlIlIIIIIl ** 0.5) + 1):
        if IllIIlIlIIIIIl % IlIIIIlIllIIIIIlIlll == 0:
            return [IlIIIIlIllIIIIIlIlll] + IIIlIlIlllIIllIIIll(IllIIlIlIIIIIl // IlIIIIlIllIIIIIlIlll)
    return []