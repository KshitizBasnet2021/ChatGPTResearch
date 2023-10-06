import math
def IlllllllIllIIlIIIIl(IIIllIllllI, IlIlIIIlIIllIlllIIl, lIIlIlIlIlll, IlIIlllIIIIIlIll):
  IlIIIllI = lIIlIlIlIlll+IlIIlllIIIIIlIll
  lllIIlIIIIIII = min(lIIlIlIlIlll+2*IlIIlllIIIIIlIll, len(IIIllIllllI))
  IIIllllIIIIIlIllI, IIIllIIlllllIllII, lIIIIlllIIIIIIl = lIIlIlIlIlll, lIIlIlIlIlll+IlIIlllIIIIIlIll, lIIlIlIlIlll
  while IIIllllIIIIIlIllI < IlIIIllI and IIIllIIlllllIllII < lllIIlIIIIIII:
    if IIIllIllllI[IIIllllIIIIIlIllI] < IIIllIllllI[IIIllIIlllllIllII]:
      IlIlIIIlIIllIlllIIl[lIIIIlllIIIIIIl] = IIIllIllllI[IIIllllIIIIIlIllI]
      IIIllllIIIIIlIllI += 1
    else:
      IlIlIIIlIIllIlllIIl[lIIIIlllIIIIIIl] = IIIllIllllI[IIIllIIlllllIllII]
      IIIllIIlllllIllII += 1
    lIIIIlllIIIIIIl += 1
  if IIIllllIIIIIlIllI > IlIIIllI:
    IlIlIIIlIIllIlllIIl[lIIIIlllIIIIIIl:lllIIlIIIIIII] = IIIllIllllI[IIIllllIIIIIlIllI:IlIIIllI]
  elif IIIllIIlllllIllII < lllIIlIIIIIII:
    IlIlIIIlIIllIlllIIl[lIIIIlllIIIIIIl:lllIIlIIIIIII] = IIIllIllllI[IIIllIIlllllIllII:lllIIlIIIIIII]
def IllllIIIllIlIlIIIII(lIIlIlIIIIIIIIlIl):
  IlIIIIIIIlI = len(lIIlIlIIIIIIIIlIl)
  IllllIIlllllI = math.ceil(math.log(IlIIIIIIIlI,2))
  IIIllIllllI, lllIIlIllIlII = lIIlIlIIIIIIIIlIl, [None] * IlIIIIIIIlI
  for lllIlIlIlIIIIIII in (2**lIlIIlIIIIll for lIlIIlIIIIll in range(IllllIIlllllI)):
    for llIllllIlIlIlll in range(0, IlIIIIIIIlI, 2*lllIlIlIlIIIIIII):
      IlllllllIllIIlIIIIl(IIIllIllllI, lllIIlIllIlII, llIllllIlIlIlll, lllIlIlIlIIIIIII)
    IIIllIllllI, lllIIlIllIlII = lllIIlIllIlII, IIIllIllllI
  if lIIlIlIIIIIIIIlIl is not IIIllIllllI:
    lIIlIlIIIIIIIIlIl[0:IlIIIIIIIlI] = IIIllIllllI[0:IlIIIIIIIlI]