from .shortest_path_lengths import shortest_path_lengths
def lIIIIIIIIIIl():
    IIIllIlIlIlllllIlIII = {
        (0, 2): 3,
        (0, 5): 5,
        (2, 1): -2,
        (2, 3): 7,
        (2, 4): 4,
        (3, 4): -5,
        (4, 5): -1
    }
    IlllIllIIlIlIIlIIIIl =  shortest_path_lengths(6, IIIllIlIlIlllllIlIII)
    for IllIlIlIlIllIIlI in IlllIllIIlIlIIlIIIIl:
        print(IllIlIlIlIllIIlI, IlllIllIIlIlIIlIIIIl[IllIlIlIlIllIIlI], end=" ")
    print()
    lIIIllIIIlI = {
        (0, 1): 3,
        (1, 2): 5,
        (2, 3): -2,
        (3, 4): 7
    }
    IlllIllIIlIlIIlIIIIl =  shortest_path_lengths(5, lIIIllIIIlI)
    for IllIlIlIlIllIIlI in IlllIllIIlIlIIlIIIIl:
        print(IllIlIlIlIllIIlI, IlllIllIIlIlIIlIIIIl[IllIlIlIlIllIIlI], end=" ")
    print()
    lllIIIlll = {
        (0, 1): 3,
        (2, 3): 5
    }
    IlllIllIIlIlIIlIIIIl =  shortest_path_lengths(4, lllIIIlll)
    for IllIlIlIlIllIIlI in IlllIllIIlIlIIlIIIIl:
        print(IllIlIlIlIllIIlI, IlllIllIIlIlIIlIIIIl[IllIlIlIlIllIIlI], end=" ")
    print()
    lIIIIIIIIlIllIlIlIlI = {
        (0, 1): 3,
        (1, 2): 5,
        (2, 0): -1
    }
    IlllIllIIlIlIIlIIIIl =  shortest_path_lengths(3, lIIIIIIIIlIllIlIlIlI)
    for IllIlIlIlIllIIlI in IlllIllIIlIlIIlIIIIl:
        print(IllIlIlIlIllIIlI, IlllIllIIlIlIIlIIIIl[IllIlIlIlIllIIlI], end=" ")
    print()
if __name__ == "__main__":
    lIIIIIIIIIIl()