import math
def lIlIllIlIIllI(lIlIlIlll, lIllIIlIIllIlllIl, IlIIIIIll, lIIIIlIII):
  IIIIIlllllIlIIIlllIl = IlIIIIIll+lIIIIlIII
  lIIlIllllllIl = min(IlIIIIIll+2*lIIIIlIII, len(lIlIlIlll))
  IIlllIlIIIIII, lllIIIIIIIIIIllIl, lllIlllIlI = IlIIIIIll, IlIIIIIll+lIIIIlIII, IlIIIIIll
  while IIlllIlIIIIII < IIIIIlllllIlIIIlllIl and lllIIIIIIIIIIllIl < lIIlIllllllIl:
    if lIlIlIlll[IIlllIlIIIIII] < lIlIlIlll[lllIIIIIIIIIIllIl]:
      lIllIIlIIllIlllIl[lllIlllIlI] = lIlIlIlll[IIlllIlIIIIII]
      IIlllIlIIIIII += 1
    else:
      lIllIIlIIllIlllIl[lllIlllIlI] = lIlIlIlll[lllIIIIIIIIIIllIl]
      lllIIIIIIIIIIllIl += 1
    lllIlllIlI += 1
  if IIlllIlIIIIII < IIIIIlllllIlIIIlllIl:
    lIllIIlIIllIlllIl[lllIlllIlI:lIIlIllllllIl] = lIlIlIlll[IIlllIlIIIIII:]
  elif lllIIIIIIIIIIllIl < lIIlIllllllIl:
    lIllIIlIIllIlllIl[lllIlllIlI:lIIlIllllllIl] = lIlIlIlll[lllIIIIIIIIIIllIl:lIIlIllllllIl]
def IlllllIllIlIIIIIIlIl(lIlIIIIl):
  IllllIIlIl = len(lIlIIIIl)
  IllllllIlIlIlIIIlI = math.ceil(math.log(IllllIIlIl,2))
  lIlIlIlll, lIllllllllI = lIlIIIIl, [None] * IllllIIlIl
  for lIllIIIll in (2**IlIIlllIlIIIIIlIII for IlIIlllIlIIIIIlIII in range(IllllllIlIlIlIIIlI)):
    for IlIlIIIIlIlI in range(0, IllllIIlIl, 2*lIllIIIll):
      lIlIllIlIIllI(lIlIlIlll, lIllllllllI, IlIlIIIIlIlI, lIllIIIll)
    lIlIlIlll, lIllllllllI = lIllllllllI, lIlIlIlll
  if lIlIIIIl is not lIlIlIlll:
    lIlIIIIl[0:IllllIIlIl] = lIlIlIlll[0:IllllIIlIl]