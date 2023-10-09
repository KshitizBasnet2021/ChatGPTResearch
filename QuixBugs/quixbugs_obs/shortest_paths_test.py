from .shortest_paths import shortest_paths
def llIIllIlIlllI():
    Illlllll = {
        ('A', 'B'): 3,
        ('A', 'C'): 3,
        ('A', 'F'): 5,
        ('C', 'B'): -2,
        ('C', 'D'): 7,
        ('C', 'E'): 4,
        ('D', 'E'): -5,
        ('E', 'F'): -1
    }
    lllIllIIlllIIIl =  shortest_paths('A', Illlllll)
    for lIIlIllllII in lllIllIIlllIIIl:
        print(lIIlIllllII, lllIllIIlllIIIl[lIIlIllllII], end=" ")
    print()
    llIlIIIIIIlIII = {
        ('A', 'B'): 1,
        ('B', 'C'): 2,
        ('C', 'D'): 3,
        ('D', 'E'): -1,
        ('E', 'F'): 4
    }
    lllIllIIlllIIIl =  shortest_paths('A', llIlIIIIIIlIII)
    for lIIlIllllII in lllIllIIlllIIIl:
        print(lIIlIllllII, lllIllIIlllIIIl[lIIlIllllII], end=" ")
    print()
    lIIIlIlllIllIllIIIl = {
        ('A', 'B'): 1,
        ('B', 'C'): 2,
        ('C', 'D'): 3,
        ('D', 'E'): -1,
        ('E', 'D'): 1,
        ('E', 'F'): 4
    }
    lllIllIIlllIIIl =  shortest_paths('A', lIIIlIlllIllIllIIIl)
    for lIIlIllllII in lllIllIIlllIIIl:
        print(lIIlIllllII, lllIllIIlllIIIl[lIIlIllllII], end=" ")
    print()
if __name__ == "__main__":
    llIIllIlIlllI()