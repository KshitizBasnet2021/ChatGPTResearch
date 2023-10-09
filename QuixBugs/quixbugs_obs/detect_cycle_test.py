from .IllIIIIlIlIIIlIl import Node
from .detect_cycle import detect_cycle
def lIlIlllllll():
    lIIlllll = Node(1)
    lllIlIIIllIlIllII = Node(2, lIIlllll)
    lIlIlllIIllllIll = Node(3, lllIlIIIllIlIllII)
    lIlllIIllIlIlIl = Node(4, lIlIlllIIllllIll)
    lIIllIIIlIIIIIIII = Node(5, lIlllIIllIlIlIl)
    if detect_cycle(lIIllIIIlIIIIIIII):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()
    lIIlllll.IIlIlIIIIlllllllll = lIIllIIIlIIIIIIII
    if detect_cycle(lIIllIIIlIIIIIIII):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()
    lIIlllll.IIlIlIIIIlllllllll = lllIlIIIllIlIllII
    if detect_cycle(lllIlIIIllIlIllII):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()
    lIIllIIIlIll = Node(6)
    lIIllIlIIllllIlIIIlI = Node(7, lIIllIIIlIll)
    if detect_cycle(lIIllIlIIllllIlIIIlI):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()
    IllIIIIlIlIIIlIl = Node(0)
    if detect_cycle(IllIIIIlIlIIIlIl):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()
    lIIlllll.IIlIlIIIIlllllllll = lllIlIIIllIlIllII
    if detect_cycle(lIIllIIIlIIIIIIII):
        print("Cycle detected!", end=" ")
    else:
        print("Cycle not detected!", end=" ")
    print()
if __name__ == "__main__":
    lIlIlllllll()