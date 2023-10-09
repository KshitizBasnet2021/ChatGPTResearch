def IIlllIlIII(IIllIlIlIlIIlllIlIIl, llllIllllll):
    from collections import defaultdict
    IllIllllllII = defaultdict(int)
    for lIIIlllIllIIIll in range(1, len(llllIllllll) + 1):
        lIllIIIIllIIlIlI, lllIIIll = llllIllllll[lIIIlllIllIIIll - 1]
        for IllllIlllIl in range(1, IIllIlIlIlIIlllIlIIl + 1):
            IllIllllllII[lIIIlllIllIIIll, IllllIlllIl] = IllIllllllII[lIIIlllIllIIIll - 1, IllllIlllIl]
            if lIllIIIIllIIlIlI < IllllIlllIl:
                IllIllllllII[lIIIlllIllIIIll, IllllIlllIl] = max(
                    IllIllllllII[lIIIlllIllIIIll, IllllIlllIl],
                    lllIIIll + IllIllllllII[lIIIlllIllIIIll - 1, IllllIlllIl - lIllIIIIllIIlIlI]
                )
    return IllIllllllII[len(llllIllllll), IIllIlIlIlIIlllIlIIl]