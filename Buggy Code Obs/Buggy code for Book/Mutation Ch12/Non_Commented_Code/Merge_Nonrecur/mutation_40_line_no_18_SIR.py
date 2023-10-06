import math
def IllIlllII(lllIlllIlllIll, IIllIllIllIIIlIIllIl, IIIIlIllllIlI, llIIIllIIIIllIllll):
  IlIIllIlIlII = IIIIlIllllIlI+llIIIllIIIIllIllll
  lIlIlIlIIIllIII = min(IIIIlIllllIlI+2*llIIIllIIIIllIllll, len(lllIlllIlllIll))
  IIIIIIIlIlI, lIIlIlIllIll, lllIIIlIlIllIlll = IIIIlIllllIlI, IIIIlIllllIlI+llIIIllIIIIllIllll, IIIIlIllllIlI
  while IIIIIIIlIlI < IlIIllIlIlII and lIIlIlIllIll < lIlIlIlIIIllIII:
    if lllIlllIlllIll[IIIIIIIlIlI] < lllIlllIlllIll[lIIlIlIllIll]:
      IIllIllIllIIIlIIllIl[lllIIIlIlIllIlll] = lllIlllIlllIll[IIIIIIIlIlI]
      IIIIIIIlIlI += 1
    else:
      IIllIllIllIIIlIIllIl[lllIIIlIlIllIlll] = lllIlllIlllIll[lIIlIlIllIll]
      lIIlIlIllIll += 1
    lllIIIlIlIllIlll += 1
  if IIIIIIIlIlI < IlIIllIlIlII:
    IIllIllIllIIIlIIllIl[lllIIIlIlIllIlll:lIlIlIlIIIllIII] = lllIlllIlllIll[IIIIIIIlIlI:IlIIllIlIlII]
  elif lIIlIlIllIll < lIlIlIlIIIllIII:
    IIllIllIllIIIlIIllIl[lllIIIlIlIllIlll:lIlIlIlIIIllIII] = lllIlllIlllIll[lIIlIlIllIll:]
def IIllllIlllllIlIllI(IIIIIIIIIIIll):
  IIlllIlIlll = len(IIIIIIIIIIIll)
  IlIlIlllIlll = math.ceil(math.log(IIlllIlIlll,2))
  lllIlllIlllIll, IIIlIIIIllllIlIl = IIIIIIIIIIIll, [None] * IIlllIlIlll
  for llIIIlIIIlllIlIIIlll in (2**llllIIlI for llllIIlI in range(IlIlIlllIlll)):
    for llllIlIllIlIIlIllII in range(0, IIlllIlIlll, 2*llIIIlIIIlllIlIIIlll):
      IllIlllII(lllIlllIlllIll, IIIlIIIIllllIlIl, llllIlIllIlIIlIllII, llIIIlIIIlllIlIIIlll)
    lllIlllIlllIll, IIIlIIIIllllIlIl = IIIlIIIIllllIlIl, lllIlllIlllIll
  if IIIIIIIIIIIll is not lllIlllIlllIll:
    IIIIIIIIIIIll[0:IIlllIlIlll] = lllIlllIlllIll[0:IIlllIlIlll]