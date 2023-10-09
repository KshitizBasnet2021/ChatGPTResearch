def IIIIlIIllIl(IllllIIlII, IIIlIlIIlllllII=1, IIIIlIlllIIllIllIIll=3):
    IlIllIllIIllIIIlI = []
    if IllllIIlII > 0:
        lllIIIIl = ({1, 2, 3} - {IIIlIlIIlllllII} - {IIIIlIlllIIllIllIIll}).pop()
        IlIllIllIIllIIIlI.extend(IIIIlIIllIl(IllllIIlII - 1, IIIlIlIIlllllII, lllIIIIl))
        IlIllIllIIllIIIlI.append((IIIlIlIIlllllII, lllIIIIl))
        IlIllIllIIllIIIlI.extend(IIIIlIIllIl(IllllIIlII - 1, lllIIIIl, IIIIlIlllIIllIllIIll))
    return IlIllIllIIllIIIlI