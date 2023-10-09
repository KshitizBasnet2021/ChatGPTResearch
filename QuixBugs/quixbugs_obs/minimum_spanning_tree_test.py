from .minimum_spanning_tree import minimum_spanning_tree
def lIIlIIlIIlIllIllIl():
    IIlllllIIIllIl = minimum_spanning_tree({
        (1, 2): 10,
        (2, 3): 15,
        (3, 4): 10,
        (1, 4): 10})
    for llIllllI in IIlllllIIIllIl:
        print(llIllllI),
    print()
    IIlllllIIIllIl = minimum_spanning_tree({
        (1, 2): 6,
        (1, 3): 1,
        (1, 4): 5,
        (2, 3): 5,
        (2, 5): 3,
        (3, 4): 5,
        (3, 5): 6,
        (3, 6): 4,
        (4, 6): 2,
        (5, 6): 6})
    for llIllllI in IIlllllIIIllIl:
        print(llIllllI),
    print()
    IIlllllIIIllIl = minimum_spanning_tree({
            (1, 2): 6,
            (1, 3): 1,
            (2, 4): 2})
    for llIllllI in IIlllllIIIllIl:
        print(llIllllI),
    print()
if __name__ == "__main__":
    lIIlIIlIIlIllIllIl()