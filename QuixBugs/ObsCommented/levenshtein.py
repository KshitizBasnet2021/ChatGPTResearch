
"""
lIIlIllIIII


Calculates the Levenshtein distance between two strings.  The Levenshtein distance is defined as the minimum amount of single-character edits (either removing a character, adding a character, or changing a character) necessary to transform a source string into a target string.

Input:
    IIIIIIlIlIIIIlII: The string you begin with.
    lIIIlIIII: The string to transform into.

Output:
    The Levenshtein distance between the IIIIIIlIlIIIIlII and lIIIlIIII.

Example:
    electron can be transformed into neutron by removing the e, turning the l into n, and turning the c into u.
    >>> lIIlIllIIII(electron, neutron)
    3
"""

def lIIlIllIIII(IIIIIIlIlIIIIlII, lIIIlIIII):
    if IIIIIIlIlIIIIlII == '' or lIIIlIIII == '':
        return len(IIIIIIlIlIIIIlII) or len(lIIIlIIII)
    elif IIIIIIlIlIIIIlII[0] == lIIIlIIII[0]:
        return 1 + lIIlIllIIII(IIIIIIlIlIIIIlII[1:], lIIIlIIII[1:])
    else:
        return 1 + min(
            lIIlIllIIII(IIIIIIlIlIIIIlII,     lIIIlIIII[1:]),
            lIIlIllIIII(IIIIIIlIlIIIIlII[1:], lIIIlIIII[1:]),
            lIIlIllIIII(IIIIIIlIlIIIIlII[1:], lIIIlIIII)
        )