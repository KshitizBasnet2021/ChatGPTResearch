from .node import Node
from .shortest_path_length import shortest_path_length
def IlIIIIlll():
    IIIIIllIllIIIlIIIlll = Node("1")
    IIlIIIIIIlIIIllIIIIl = Node("5")
    llIlllIlIllIlIllIlII = Node("4", None, [IIlIIIIIIlIIIllIIIIl])
    IllIllllI = Node("3", None, [llIlllIlIllIlIllIlII])
    IlIIIIlIlllIlIIlIl = Node("2", None, [IIIIIllIllIIIlIIIlll, IllIllllI, llIlllIlIllIlIllIlII])
    lIIlIlIIIIlIIIlIlII = Node("0", None, [IlIIIIlIlllIlIIlIl, IIlIIIIIIlIIIllIIIIl])
    lIIlllIlIllIIlI = {
        (lIIlIlIIIIlIIIlIlII, IlIIIIlIlllIlIIlIl): 3,
        (lIIlIlIIIIlIIIlIlII, IIlIIIIIIlIIIllIIIIl): 10,
        (IlIIIIlIlllIlIIlIl, IIIIIllIllIIIlIIIlll): 1,
        (IlIIIIlIlllIlIIlIl, IllIllllI): 2,
        (IlIIIIlIlllIlIIlIl, llIlllIlIllIlIllIlII): 4,
        (IllIllllI, llIlllIlIllIlIllIlII): 1,
        (llIlllIlIllIlIllIlII, IIlIIIIIIlIIIllIIIIl): 1
    }
    IlllIllIIlllIlIIIlI =  shortest_path_length(lIIlllIlIllIIlI, lIIlIlIIIIlIIIlIlII, IIIIIllIllIIIlIIIlll)
    print(IlllIllIIlllIlIIIlI)
    IlllIllIIlllIlIIIlI = shortest_path_length(lIIlllIlIllIIlI, lIIlIlIIIIlIIIlIlII, IIlIIIIIIlIIIllIIIIl)
    print(IlllIllIIlllIlIIIlI)
    IlllIllIIlllIlIIIlI = shortest_path_length(lIIlllIlIllIIlI, IlIIIIlIlllIlIIlIl, IlIIIIlIlllIlIIlIl)
    print(IlllIllIIlllIlIIIlI)
    IlllIllIIlllIlIIIlI = shortest_path_length(lIIlllIlIllIIlI, IIIIIllIllIIIlIIIlll, IIlIIIIIIlIIIllIIIIl)
    print(IlllIllIIlllIlIIIlI)
if __name__ == "__main__":
    IlIIIIlll()