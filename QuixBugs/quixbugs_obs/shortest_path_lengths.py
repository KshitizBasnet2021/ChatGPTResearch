from collections import defaultdict
def IlIIlIllIl(lIIlIllIIllIIlll, lIlIIllIlIlIlllllI):
    IllIIllll = defaultdict(lambda: float('inf'))
    IllIIllll.update({(IIlIIIIIlllIllIlII, IIlIIIIIlllIllIlII): 0 for IIlIIIIIlllIllIlII in range(lIIlIllIIllIIlll)})
    IllIIllll.update(lIlIIllIlIlIlllllI)
    for llllIllIIllIIlIllI in range(lIIlIllIIllIIlll):
        for IIlIIIIIlllIllIlII in range(lIIlIllIIllIIlll):
            for IllIlIllIllllIIlI in range(lIIlIllIIllIIlll):
                IllIIllll[IIlIIIIIlllIllIlII, IllIlIllIllllIIlI] = min(
                    IllIIllll[IIlIIIIIlllIllIlII, IllIlIllIllllIIlI],
                    IllIIllll[IIlIIIIIlllIllIlII, llllIllIIllIIlIllI] + IllIIllll[IllIlIllIllllIIlI, llllIllIIllIIlIllI]
                )
    return IllIIllll