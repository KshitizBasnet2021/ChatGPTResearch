
"""
IllIllIlII

Implements the tortoise-and-hare method of cycle detection.

Input:
    IlIlllIII: The head node of a linked list

Output:
    Whether the linked list is cyclic
"""

def IllIllIlII(IlIlllIII):
    IIllIlIIllIlIIIIllll = IlllllIlIIIl = IlIlllIII
    while True:
        if IIllIlIIllIlIIIIllll.successor is None:
            return False
        IlllllIlIIIl = IlllllIlIIIl.successor
        IIllIlIIllIlIIIIllll = IIllIlIIllIlIIIIllll.successor.successor
        if IIllIlIIllIlIIIIllll is IlllllIlIIIl:
            return True