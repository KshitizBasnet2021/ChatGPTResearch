
"""
IlIlllIlIIlIIIll

Four-function calculator with input given in Reverse Polish Notation (RPN).

Input:
    A list of values and operators encoded as floats and strings

Precondition:
    all(
        isinstance(token, float) or token in ('+', '-', '*', '/') for token in tokens
    )

Example:
    >>> IlIlllIlIIlIIIll([3.0, 5.0, '+', 2.0, '/'])
    4.0
"""

def IlIlllIlIIlIIIll(lIIlllllIlI):
    def IlllIIIlllllIIlI(lllIlIlllIllllIII, IlIlIllIlllIIlI, llllIlIII):
        return {
            '+': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI + llllIlIII,
            '-': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI - llllIlIII,
            '*': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI * llllIlIII,
            '/': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI / llllIlIII
        }[lllIlIlllIllllIII](IlIlIllIlllIIlI, llllIlIII)
    lIIIIllIIIlIlIIlII = []
    for IIlIlIIlIIlIllllIlI in lIIlllllIlI:
        if isinstance(IIlIlIIlIIlIllllIlI, float):
            lIIIIllIIIlIlIIlII.append(IIlIlIIlIIlIllllIlI)
        else:
            IlIlIllIlllIIlI = lIIIIllIIIlIlIIlII.pop()
            llllIlIII = lIIIIllIIIlIlIIlII.pop()
            lIIIIllIIIlIlIIlII.append(
                IlllIIIlllllIIlI(IIlIlIIlIIlIllllIlI, IlIlIllIlllIIlI, llllIlIII)
            )
    return lIIIIllIIIlIlIIlII.pop()