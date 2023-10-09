from collections import deque as Queue
def IlllIlIIIllllIIIII(IlIIIIlIIlIIIl, llllIlllIIIIllIlI):
    IlIlllllllIIIIlIIIII = Queue()
    IlIlllllllIIIIlIIIII.append(IlIIIIlIIlIIIl)
    IIIllIIlllIl = set()
    IIIllIIlllIl.add(IlIIIIlIIlIIIl)
    while True:
        IlllIIlIIIIIlIll = IlIlllllllIIIIlIIIII.popleft()
        if IlllIIlIIIIIlIll is llllIlllIIIIllIlI:
            return True
        else:
            IlIlllllllIIIIlIIIII.extend(IlllIIlIIIIIlIll for IlllIIlIIIIIlIll in IlllIIlIIIIIlIll.successors if IlllIIlIIIIIlIll not in IIIllIIlllIl)
            IIIllIIlllIl.update(IlllIIlIIIIIlIll.successors)
    return False