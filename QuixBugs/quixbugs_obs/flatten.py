def lllIIIlll(IlIIlIIllll):
    for IIlIlIIIll in IlIIlIIllll:
        if isinstance(IIlIlIIIll, list):
            for IIIlIIlllI in lllIIIlll(IIlIlIIIll):
                yield IIIlIIlllI
        else:
            yield lllIIIlll(IIlIlIIIll)