
"""
lIIIIlIllIIIIIIlIlII

Reverses a linked list and returns the new head.

Input:
    IIlllIIIlIlllIl: The head of a singly-linked list

Precondition:
    The input is acyclic

Side effect:
    Mutates the list IIlllIIIlIlllIls' successor pointers

Output:
    The head of the reversed linked list
"""

def lIIIIlIllIIIIIIlIlII(IIlllIIIlIlllIl):
    llIlIIlIIIl = None
    while IIlllIIIlIlllIl:
        IlIlIlIIllIIlIIII = IIlllIIIlIlllIl.IlIIlIIIllllIIlIlIIl
        IIlllIIIlIlllIl.IlIIlIIIllllIIlIlIIl = llIlIIlIIIl
        IIlllIIIlIlllIl = IlIlIlIIllIIlIIII
    return llIlIIlIIIl