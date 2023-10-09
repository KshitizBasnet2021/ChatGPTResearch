def IlllIIIllII(IIllIllII, IlIlllIllllIIIIll):
    import heapq
    IlIIllllII = IIllIllII[:IlIlllIllllIIIIll]
    heapq.heapify(IlIIllllII)
    for IlIIllIIllIIlI in IIllIllII:
        yield heapq.heappushpop(IlIIllllII, IlIIllIIllIIlI)
    while IlIIllllII:
        yield heapq.heappop(IlIIllllII)