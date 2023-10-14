
"""
IlIllllIIIllIlIl
Input:
    lIllIlIIIllII: A string of parentheses

Precondition:
    all(paren in '()' for paren in lIllIlIIIllII)

Output:
    Whether the parentheses are properly nested

Examples:
    >>> IlIllllIIIllIlIl('((()()))()')
    True
    >>> IlIllllIIIllIlIl(')()(')
    False
"""

def IlIllllIIIllIlIl(lIllIlIIIllII):
    IlllIIlIIlIl = 0
    for IlIlIIlIllIllI in lIllIlIIIllII:
        if IlIlIIlIllIllI == '(':
            IlllIIlIIlIl += 1
        else:
            IlllIIlIIlIl -= 1
            if IlllIIlIIlIl < 0:
                return False
    return True