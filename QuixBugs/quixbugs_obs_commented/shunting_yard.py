
"""
Infix to RPN Conversion
IllllIll


Uses Dijkstra's shunting-yard algorithm to transform infix notation into equivalent Reverse Polish Notation.

Input:
    lIllllIll: A list of tokens in infix notation

Precondition:
    all(isinstance(lIllllIll, int) or token in '+-*/' for token in lIllllIll)

Output:
    The input lIllllIll reordered into Reverse Polish Notation

Examples:
    >>> IllllIll([10, '-', 5, '-', 2])
    [10, 5, '-', 2, '-']
    >>> IllllIll([34, '-', 12, '/', 5])
    [34, 12, 5, '/' ,'-']
    >>> IllllIll([4, '+', 9, '*', 9, '-', 10, '+', 13])
    [4, 9, 9, '*', '+', 10, '-', 13, '+']
"""

def IllllIll(lIllllIll):
    lIllllIlIIII = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    lIlIlIlIIlIlIlIIllI = []
    lIIlllIllIlllIlIIlII = []
    for IlllIlIIl in lIllllIll:
        if isinstance(IlllIlIIl, int):
            lIlIlIlIIlIlIlIIllI.append(IlllIlIIl)
        else:
            while lIIlllIllIlllIlIIlII and lIllllIlIIII[IlllIlIIl] <= lIllllIlIIII[lIIlllIllIlllIlIIlII[-1]]:
                lIlIlIlIIlIlIlIIllI.append(lIIlllIllIlllIlIIlII.pop())
    while lIIlllIllIlllIlIIlII:
        lIlIlIlIIlIlIlIIllI.append(lIIlllIllIlllIlIIlII.pop())
    return lIlIlIlIIlIlIlIIllI