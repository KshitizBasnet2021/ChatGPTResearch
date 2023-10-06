import math
def IIIIlllIlIlIIll(IIlIllIlIl, IIIlllIIllIlIIllIll, IIIIlIIIIIllII, IIlIlIlIlIll):
  IlIIllllllI = IIIIlIIIIIllII+IIlIlIlIlIll
  lIllIIllIlllIlllll = min(IIIIlIIIIIllII+2*IIlIlIlIlIll, len(IIlIllIlIl))
  lIlllllIllI, llIllIllI, IlIIlIlllIlllI = IIIIlIIIIIllII, IIIIlIIIIIllII+IIlIlIlIlIll, IIIIlIIIIIllII
  while (lIlllllIllI < IlIIllllllI or llIllIllI < lIllIIllIlllIlllll):
    if IIlIllIlIl[lIlllllIllI] < IIlIllIlIl[llIllIllI]:
      IIIlllIIllIlIIllIll[IlIIlIlllIlllI] = IIlIllIlIl[lIlllllIllI]
      lIlllllIllI += 1
    else:
      IIIlllIIllIlIIllIll[IlIIlIlllIlllI] = IIlIllIlIl[llIllIllI]
      llIllIllI += 1
    IlIIlIlllIlllI += 1
  if lIlllllIllI < IlIIllllllI:
    IIIlllIIllIlIIllIll[IlIIlIlllIlllI:lIllIIllIlllIlllll] = IIlIllIlIl[lIlllllIllI:IlIIllllllI]
  elif llIllIllI < lIllIIllIlllIlllll:
    IIIlllIIllIlIIllIll[IlIIlIlllIlllI:lIllIIllIlllIlllll] = IIlIllIlIl[llIllIllI:lIllIIllIlllIlllll]
def llIIlIlIlllIlIlIIll(lIIIlIllIIlIllIlIlI):
  lllIlllI = len(lIIIlIllIIlIllIlIlI)
  IIlIIllI = math.ceil(math.log(lllIlllI,2))
  IIlIllIlIl, IlIlIIlIlllII = lIIIlIllIIlIllIlIlI, [None] * lllIlllI
  for lllllllIll in (2**llIIIlIIIlIIllIll for llIIIlIIIlIIllIll in range(IIlIIllI)):
    for lIIlIlIllIIlIllIlIII in range(0, lllIlllI, 2*lllllllIll):
      IIIIlllIlIlIIll(IIlIllIlIl, IlIlIIlIlllII, lIIlIlIllIIlIllIlIII, lllllllIll)
    IIlIllIlIl, IlIlIIlIlllII = IlIlIIlIlllII, IIlIllIlIl
  if lIIIlIllIIlIllIlIlI is not IIlIllIlIl:
    lIIIlIllIIlIllIlIlI[0:lllIlllI] = IIlIllIlIl[0:lllIlllI]