def IllIllIIlIIllIIIll(lIIIlIIIIlllIl):
    lIIIlIIIlllIIIlII = {}
    IIIIIllIIIIIlII = set()
    for llllIIIIIIll in sorted(lIIIlIIIIlllIl, key=lIIIlIIIIlllIl.__getitem__):
        IlllIlllll, lIIlIIll = llllIIIIIIll
        if lIIIlIIIlllIIIlII.setdefault(IlllIlllll, {IlllIlllll}) != lIIIlIIIlllIIIlII.setdefault(lIIlIIll, {lIIlIIll}):
            IIIIIllIIIIIlII.add(llllIIIIIIll)
            lIIIlIIIlllIIIlII[IlllIlllll].update(lIIIlIIIlllIIIlII[lIIlIIll])
            for IlIIIllllIIllllll in lIIIlIIIlllIIIlII[lIIlIIll]:
                lIIIlIIIlllIIIlII[IlIIIllllIIllllll].update(lIIIlIIIlllIIIlII[IlllIlllll])
    return IIIIIllIIIIIlII