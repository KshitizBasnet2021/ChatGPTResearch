from .node import Node
from .topological_ordering import topological_ordering
def lIlllllIIlIllI():
    IIIlIIIl = Node(5)
    IIlIIlIIll = Node(7)
    IIIIIlIIlIIlIIlII = Node(3)
    IIlllIIIlIlIIllIlI = Node(11)
    lIllIlIlllIllIll = Node(8)
    llIIlIIlIlIIlIlIIIIl = Node(2)
    IIIllIIlI = Node(9)
    llIIIlIIllllIl = Node(10)
    IIIlIIIl.IllIIllIIIllllllllll = [IIlllIIIlIlIIllIlI]
    IIlIIlIIll.IllIIllIIIllllllllll = [IIlllIIIlIlIIllIlI, lIllIlIlllIllIll]
    IIIIIlIIlIIlIIlII.IllIIllIIIllllllllll = [lIllIlIlllIllIll, llIIIlIIllllIl]
    IIlllIIIlIlIIllIlI.llIlIIllllllIIlIlI = [IIIlIIIl, IIlIIlIIll]
    IIlllIIIlIlIIllIlI.IllIIllIIIllllllllll = [llIIlIIlIlIIlIlIIIIl, IIIllIIlI, llIIIlIIllllIl]
    lIllIlIlllIllIll.llIlIIllllllIIlIlI = [IIlIIlIIll, IIIIIlIIlIIlIIlII]
    lIllIlIlllIllIll.IllIIllIIIllllllllll = [IIIllIIlI]
    llIIlIIlIlIIlIlIIIIl.llIlIIllllllIIlIlI = [IIlllIIIlIlIIllIlI]
    IIIllIIlI.llIlIIllllllIIlIlI = [IIlllIIIlIlIIllIlI, lIllIlIlllIllIll]
    llIIIlIIllllIl.llIlIIllllllIIlIlI = [IIlllIIIlIlIIllIlI, IIIIIlIIlIIlIIlII]
    try:
        [print(IIIlIIllllllI.value, end=" ") for IIIlIIllllllI in topological_ordering([IIIlIIIl, IIlIIlIIll, IIIIIlIIlIIlIIlII, IIlllIIIlIlIIllIlI, lIllIlIlllIllIll, llIIlIIlIlIIlIlIIIIl, IIIllIIlI, llIIIlIIllllIl])]
    except Exception as e:
        print(e)
    print()
    IIIlIIIl = Node(5)
    IIIlllIlIlIllIIl = Node(0)
    lIlllIIllllIlIIlI = Node(4)
    IlIlIIIlI = Node(1)
    llIIlIIlIlIIlIlIIIIl = Node(2)
    IIIIIlIIlIIlIIlII = Node(3)
    IIIlIIIl.IllIIllIIIllllllllll = [llIIlIIlIlIIlIlIIIIl, IIIlllIlIlIllIIl]
    lIlllIIllllIlIIlI.IllIIllIIIllllllllll = [IIIlllIlIlIllIIl, IlIlIIIlI]
    llIIlIIlIlIIlIlIIIIl.llIlIIllllllIIlIlI = [IIIlIIIl]
    llIIlIIlIlIIlIlIIIIl.IllIIllIIIllllllllll = [IIIIIlIIlIIlIIlII]
    IIIlllIlIlIllIIl.llIlIIllllllIIlIlI = [IIIlIIIl, lIlllIIllllIlIIlI]
    IlIlIIIlI.llIlIIllllllIIlIlI = [lIlllIIllllIlIIlI, IIIIIlIIlIIlIIlII]
    IIIIIlIIlIIlIIlII.llIlIIllllllIIlIlI = [llIIlIIlIlIIlIlIIIIl]
    IIIIIlIIlIIlIIlII.IllIIllIIIllllllllll = [IlIlIIIlI]
    try:
        [print(IIIlIIllllllI.value, end=" ") for IIIlIIllllllI in topological_ordering([IIIlllIlIlIllIIl, IlIlIIIlI, llIIlIIlIlIIlIlIIIIl, IIIIIlIIlIIlIIlII, lIlllIIllllIlIIlI, IIIlIIIl])]
    except Exception as e:
        print(e)
    print()
    llIllllIIllIIIIl = Node("3/4 cup milk")
    IllIlIlIII = Node("1 egg")
    llIIllIllIlIIll = Node("1 Tbl oil")
    llIIIlllII = Node("1 cup mix")
    llIIlIIl = Node("heat syrup")
    IlIlllIlIl = Node("heat griddle")
    lIlIlIllIIl = Node("pour 1/4 cup")
    lIlIlIIlllIIlIlllII = Node("turn when bubbly")
    llIlIIIlIIll = Node("eat")
    llIllllIIllIIIIl.IllIIllIIIllllllllll = [llIIIlllII]
    IllIlIlIII.IllIIllIIIllllllllll = [llIIIlllII]
    llIIllIllIlIIll.IllIIllIIIllllllllll = [llIIIlllII]
    llIIIlllII.llIlIIllllllIIlIlI = [llIllllIIllIIIIl, IllIlIlIII, llIIllIllIlIIll]
    llIIIlllII.IllIIllIIIllllllllll = [llIIlIIl, lIlIlIllIIl]
    IlIlllIlIl.IllIIllIIIllllllllll = [lIlIlIllIIl]
    lIlIlIllIIl.llIlIIllllllIIlIlI = [llIIIlllII, IlIlllIlIl]
    lIlIlIllIIl.IllIIllIIIllllllllll = [lIlIlIIlllIIlIlllII]
    lIlIlIIlllIIlIlllII.llIlIIllllllIIlIlI = [lIlIlIllIIl]
    lIlIlIIlllIIlIlllII.IllIIllIIIllllllllll = [llIlIIIlIIll]
    llIIlIIl.llIlIIllllllIIlIlI = [llIIIlllII]
    llIIlIIl.IllIIllIIIllllllllll = [llIlIIIlIIll]
    llIlIIIlIIll.llIlIIllllllIIlIlI = [llIIlIIl, lIlIlIIlllIIlIlllII]
    try:
        [print(IIIlIIllllllI.value, end=" ") for IIIlIIllllllI in topological_ordering([llIllllIIllIIIIl, IllIlIlIII, llIIllIllIlIIll, llIIIlllII, llIIlIIl, IlIlllIlIl, lIlIlIllIIl, lIlIlIIlllIIlIlllII, llIlIIIlIIll])]
    except Exception as e:
        print(e)
    print()
if __name__ == "__main__":
    lIlllllIIlIllI()