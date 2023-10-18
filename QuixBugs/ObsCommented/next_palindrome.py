
"""
lIlIllIIl
Finds the next palindromic integer when given the current integer
Integers are stored as arrays of base 10 digits from most significant to least significant

Input:
    lIllIIIIIllIIIIIlII: An array representing the current palindrome

Output:
    An array which represents the next palindrome

Preconditions:
    The initial input array represents a palindrome

Example
    >>> lIlIllIIl([1,4,9,4,1])
    [1,5,0,5,1]
"""

def lIlIllIIl(lIllIIIIIllIIIIIlII):
    IIllllll = len(lIllIIIIIllIIIIIlII) // 2
    IIlIlIlIllI = (len(lIllIIIIIllIIIIIlII) - 1) // 2
    while IIllllll < len(lIllIIIIIllIIIIIlII) and IIlIlIlIllI >= 0:
        if lIllIIIIIllIIIIIlII[IIllllll] == 9:
            lIllIIIIIllIIIIIlII[IIllllll] = 0
            lIllIIIIIllIIIIIlII[IIlIlIlIllI] = 0
            IIllllll += 1
            IIlIlIlIllI -= 1
        else:
            lIllIIIIIllIIIIIlII[IIllllll] += 1
            if IIlIlIlIllI != IIllllll:
                lIllIIIIIllIIIIIlII[IIlIlIlIllI] += 1
            return lIllIIIIIllIIIIIlII
    return [1] + (len(lIllIIIIIllIIIIIlII)) * [0] + [1]