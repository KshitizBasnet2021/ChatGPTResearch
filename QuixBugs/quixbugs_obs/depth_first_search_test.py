from .node import Node
from .depth_first_search import depth_first_search
def llllIIIlIlIllIIl():
    lIIIIIIllll = Node("Westminster")
    lIlIIIIllIIIIIlllIlI = Node("Waterloo", None, [lIIIIIIllll])
    lIIIIIlIIl = Node("Trafalgar Square", None, [lIIIIIIllll, lIlIIIIllIIIIIlllIlI])
    IIIlIIIlllIIIIllll = Node("Canary Wharf",  None, [lIlIIIIllIIIIIlllIlI, lIIIIIlIIl])
    lllIlllIIlIIIlll = Node("London Bridge",  None, [IIIlIIIlllIIIIllll, lIIIIIlIIl])
    lllIlIllIlIlIIIIlII = Node("Tottenham Court Road",  None, [lllIlllIIlIIIlll, IIIlIIIlllIIIIllll])
    if depth_first_search(lllIlIllIlIlIIIIlII, lIIIIIIllll):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    IlIllllIIIl =  Node("F")
    llllIIllIIIllIl =  Node("E")
    lIIIlllIllIIIIllIll =  Node("D")
    llIIlllllI =  Node("C", None, [IlIllllIIIl])
    IIIIllIlIllllII =  Node("B", None, [llllIIllIIIllIl])
    IlIIlIIlIII =  Node("A", None, [IIIIllIlIllllII, llIIlllllI, lIIIlllIllIIIIllIll])
    if depth_first_search(IlIIlIIlIII, llllIIllIIIllIl):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    if depth_first_search(IlIllllIIIl, llllIIllIIIllIl):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    if depth_first_search(IlIllllIIIl, IlIllllIIIl):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    llllIIllIIIllIl.lllIIIIllIIIIIlII = [IlIIlIIlIII]
    if depth_first_search(IlIIlIIlIII, IlIllllIIIl):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
if __name__ == "__main__":
    llllIIIlIlIllIIl()