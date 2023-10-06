import math
def lllIIlIIlIlllIlII(IlIIIIlII, lIllIIIlIllIllll, lIIlIIIIllIIIII, lIIIIIIllIlIIlIlI):
  IllIlllI = lIIlIIIIllIIIII+lIIIIIIllIlIIlIlI
  IIlllIIIII = min(lIIlIIIIllIIIII+2*lIIIIIIllIlIIlIlI, len(IlIIIIlII))
  IIlIIlIllllIlIIl, lllllIlllllIIIIl, lIIlIIllIlI = lIIlIIIIllIIIII, lIIlIIIIllIIIII+lIIIIIIllIlIIlIlI, lIIlIIIIllIIIII
  while (IIlIIlIllllIlIIl <= IllIlllI and lllllIlllllIIIIl < IIlllIIIII):
    if IlIIIIlII[IIlIIlIllllIlIIl] < IlIIIIlII[lllllIlllllIIIIl]:
      lIllIIIlIllIllll[lIIlIIllIlI] = IlIIIIlII[IIlIIlIllllIlIIl]
      IIlIIlIllllIlIIl += 1
    else:
      lIllIIIlIllIllll[lIIlIIllIlI] = IlIIIIlII[lllllIlllllIIIIl]
      lllllIlllllIIIIl += 1
    lIIlIIllIlI += 1
  if IIlIIlIllllIlIIl < IllIlllI:
    lIllIIIlIllIllll[lIIlIIllIlI:IIlllIIIII] = IlIIIIlII[IIlIIlIllllIlIIl:IllIlllI]
  elif lllllIlllllIIIIl < IIlllIIIII:
    lIllIIIlIllIllll[lIIlIIllIlI:IIlllIIIII] = IlIIIIlII[lllllIlllllIIIIl:IIlllIIIII]
def IllllllIIIllIIIIIIll(IlIIIlIII):
  lllIlllII = len(IlIIIlIII)
  IIIlIlIllllIIlIIIll = math.ceil(math.log(lllIlllII,2))
  IlIIIIlII, lllIlllIIlllI = IlIIIlIII, [None] * lllIlllII
  for lIIIlllIlIllIl in (2**lIlllIllIIlIl for lIlllIllIIlIl in range(IIIlIlIllllIIlIIIll)):
    for lllIIIIIIIIIIIIIl in range(0, lllIlllII, 2*lIIIlllIlIllIl):
      lllIIlIIlIlllIlII(IlIIIIlII, lllIlllIIlllI, lllIIIIIIIIIIIIIl, lIIIlllIlIllIl)
    IlIIIIlII, lllIlllIIlllI = lllIlllIIlllI, IlIIIIlII
  if IlIIIlIII is not IlIIIIlII:
    IlIIIlIII[0:lllIlllII] = IlIIIIlII[0:lllIlllII]