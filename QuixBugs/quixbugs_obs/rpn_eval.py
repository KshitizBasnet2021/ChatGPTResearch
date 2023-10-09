def IlIlllIlIIlIIIll(lIIlllllIlI):
    def IlllIIIlllllIIlI(lllIlIlllIllllIII, IlIlIllIlllIIlI, llllIlIII):
        return {
            '+': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI + llllIlIII,
            '-': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI - llllIlIII,
            '*': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI * llllIlIII,
            '/': lambda IlIlIllIlllIIlI, llllIlIII: IlIlIllIlllIIlI / llllIlIII
        }[lllIlIlllIllllIII](IlIlIllIlllIIlI, llllIlIII)
    lIIIIllIIIlIlIIlII = []
    for IIlIlIIlIIlIllllIlI in lIIlllllIlI:
        if isinstance(IIlIlIIlIIlIllllIlI, float):
            lIIIIllIIIlIlIIlII.append(IIlIlIIlIIlIllllIlI)
        else:
            IlIlIllIlllIIlI = lIIIIllIIIlIlIIlII.pop()
            llllIlIII = lIIIIllIIIlIlIIlII.pop()
            lIIIIllIIIlIlIIlII.append(
                IlllIIIlllllIIlI(IIlIlIIlIIlIllllIlI, IlIlIllIlllIIlI, llllIlIII)
            )
    return lIIIIllIIIlIlIIlII.pop()