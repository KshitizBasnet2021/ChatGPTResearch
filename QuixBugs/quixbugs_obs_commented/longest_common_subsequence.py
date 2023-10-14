
"""
lIIIllIII


Calculates the longest subsequence common to the two input strings. (A subsequence is any sequence of letters in the same order
they appear in the string, possibly skipping letters in between.)

Input:
    lllIIIlII: The first string to consider.
    IIIlIIIIlIIllIlll: The second string to consider.

Output:
    The longest string which is a subsequence of both strings. (If multiple subsequences of equal length exist, either is OK.)

Example:
    >>> lIIIllIII('headache', 'pentadactyl')
    'eadac'
"""

def lIIIllIII(lllIIIlII, IIIlIIIIlIIllIlll):
    if not lllIIIlII or not IIIlIIIIlIIllIlll:
        return ''
    elif lllIIIlII[0] == IIIlIIIIlIIllIlll[0]:
        return lllIIIlII[0] + lIIIllIII(lllIIIlII[1:], IIIlIIIIlIIllIlll)
    else:
        return max(
            lIIIllIII(lllIIIlII, IIIlIIIIlIIllIlll[1:]),
            lIIIllIII(lllIIIlII[1:], IIIlIIIIlIIllIlll),
            key=len
        )