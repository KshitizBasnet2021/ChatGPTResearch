
"""
lIlIIlllIllIlllI

Given a long string and a column width, break the string on spaces into a list of lines such that each line is no longer than the column width.

Input:
    IlllIIIlllIllIIIlI: The starting text.
    IlIllIIlIIIlIIlIIII: The target column width, i.e. the maximum length of any single line after wrapping.

Precondition:
    IlIllIIlIIIlIIlIIII > 0.

Output:
    An ordered list of strings, each no longer than the column width, such that the concatenation of the strings returns the original text,
and such that no word in the original text is broken into two parts unless necessary.  The original amount of spaces are preserved (e.g. spaces
at the start or end of each line aren't trimmed.),Wrapping Text
"""

def lIlIIlllIllIlllI(IlllIIIlllIllIIIlI, IlIllIIlIIIlIIlIIII):
    IllIlllIl = []
    while len(IlllIIIlllIllIIIlI) > IlIllIIlIIIlIIlIIII:
        lllIIIllIlIllIlIll = IlllIIIlllIllIIIlI.rfind(' ', 0, IlIllIIlIIIlIIlIIII + 1)
        if lllIIIllIlIllIlIll == -1:
            lllIIIllIlIllIlIll = IlIllIIlIIIlIIlIIII
        IllllIIIllIII, IlllIIIlllIllIIIlI = IlllIIIlllIllIIIlI[:lllIIIllIlIllIlIll], IlllIIIlllIllIIIlI[lllIIIllIlIllIlIll:]
        IllIlllIl.append(IllllIIIllIII)
    return IllIlllIl