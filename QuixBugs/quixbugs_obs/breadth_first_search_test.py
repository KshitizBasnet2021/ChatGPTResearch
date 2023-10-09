from .node import Node
from .breadth_first_search import breadth_first_search
def IlIIIIIlllI():
    IIIlIllIIlIllllllll = Node("Westminster")
    llIIlIllIIllll = Node("Waterloo", None, [IIIlIllIIlIllllllll])
    IlllIlIllIIIlI = Node("Trafalgar Square", None, [IIIlIllIIlIllllllll, llIIlIllIIllll])
    llIIlIIlllIIlIllIll = Node("Canary Wharf",  None, [llIIlIllIIllll, IlllIlIllIIIlI])
    lIIIllIllllII = Node("London Bridge",  None, [llIIlIIlllIIlIllIll, IlllIlIllIIIlI])
    lllIIlIllIIIIIl = Node("Tottenham Court Road",  None, [lIIIllIllllII, llIIlIIlllIIlIllIll])
    if breadth_first_search(lllIIlIllIIIIIl, IIIlIllIIlIllllllll):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    IlIlllIllIllIl =  Node("F")
    IIlIIlIIIllIlIlllIl =  Node("E")
    lIIIlIIll =  Node("D")
    IllIIIIlIIlIll =  Node("C", None, [IlIlllIllIllIl])
    llllIlllIlIlIl =  Node("B", None, [IIlIIlIIIllIlIlllIl])
    IlIIIlllllIllIll =  Node("A", None, [llllIlllIlIlIl, IllIIIIlIIlIll, lIIIlIIll])
    if breadth_first_search(IlIIIlllllIllIll, IIlIIlIIIllIlIlllIl):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    if breadth_first_search(IlIlllIllIllIl, IIlIIlIIIllIlIlllIl):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    if breadth_first_search(IlIlllIllIllIl, IlIlllIllIllIl):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
    llIllIIIlIIllIIll = Node("1")
    llIlIlIIlIlI = Node("2")
    llIllIllllIlIIIIll = Node("3")
    lIIlIlllllIIl = Node("4", None, [llIllIIIlIIllIIll])
    IllIlIlIIlll = Node("5", None, [llIlIlIIlIlI])
    lIlIllIIllI = Node("6", None, [IllIlIlIIlll, lIIlIlllllIIl, llIllIllllIlIIIIll])
    llIlIlIIlIlI.llllIIllI = [lIlIllIIllI]
    if breadth_first_search(lIlIllIIllI, llIllIIIlIIllIIll):
        print("Path found!", end=" ")
    else:
        print("Path not found!", end=" ")
    print()
if __name__ == "__main__":
    IlIIIIIlllI()