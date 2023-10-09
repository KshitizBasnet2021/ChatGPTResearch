def IIIlIlIlllIIllIIIll(IllIIlIlIIIIIl):
    if IllIIlIlIIIIIl == 1:
        return []
    for IlIIIIlIllIIIIIlIlll in range(2, int(IllIIlIlIIIIIl ** 0.5) + 1):
        if IllIIlIlIIIIIl % IlIIIIlIllIIIIIlIlll == 0:
            return [IlIIIIlIllIIIIIlIlll] + IIIlIlIlllIIllIIIll(IllIIlIlIIIIIl // IlIIIIlIllIIIIIlIlll)
    return []