import math
def IlIIlIlIIIlIlIl(lIlIIlII, lIllllIlllllIII, lllIlIllllIIlIIlI, IllIIllII):
  llllIlIIlIIIll = lllIlIllllIIlIIlI+IllIIllII
  IlIlIIIIlI = min(lllIlIllllIIlIIlI + (2 ** IllIIllII), len(lIlIIlII))
  lIlIlIIIIIlIIIIlllII, llIllIlIIlllIlllIl, IlIllIII = lllIlIllllIIlIIlI, lllIlIllllIIlIIlI+IllIIllII, lllIlIllllIIlIIlI
  while lIlIlIIIIIlIIIIlllII < llllIlIIlIIIll and llIllIlIIlllIlllIl < IlIlIIIIlI:
    if lIlIIlII[lIlIlIIIIIlIIIIlllII] < lIlIIlII[llIllIlIIlllIlllIl]:
      lIllllIlllllIII[IlIllIII] = lIlIIlII[lIlIlIIIIIlIIIIlllII]
      lIlIlIIIIIlIIIIlllII += 1
    else:
      lIllllIlllllIII[IlIllIII] = lIlIIlII[llIllIlIIlllIlllIl]
      llIllIlIIlllIlllIl += 1
    IlIllIII += 1
  if lIlIlIIIIIlIIIIlllII < llllIlIIlIIIll:
    lIllllIlllllIII[IlIllIII:IlIlIIIIlI] = lIlIIlII[lIlIlIIIIIlIIIIlllII:llllIlIIlIIIll]
  elif llIllIlIIlllIlllIl < IlIlIIIIlI:
    lIllllIlllllIII[IlIllIII:IlIlIIIIlI] = lIlIIlII[llIllIlIIlllIlllIl:IlIlIIIIlI]
def lIIIllllIlIlIIlll(lIllllllIIlll):
  IIIllIIll = len(lIllllllIIlll)
  lIlIIIIlIII = math.ceil(math.log(IIIllIIll,2))
  lIlIIlII, IIIlIIIIIllllIIl = lIllllllIIlll, [None] * IIIllIIll
  for lIlIlIIlIIlIIl in (2**lIIllIllIIIIIlllllI for lIIllIllIIIIIlllllI in range(lIlIIIIlIII)):
    for lIlIIllII in range(0, IIIllIIll, 2*lIlIlIIlIIlIIl):
      IlIIlIlIIIlIlIl(lIlIIlII, IIIlIIIIIllllIIl, lIlIIllII, lIlIlIIlIIlIIl)
    lIlIIlII, IIIlIIIIIllllIIl = IIIlIIIIIllllIIl, lIlIIlII
  if lIllllllIIlll is not lIlIIlII:
    lIllllllIIlll[0:IIIllIIll] = lIlIIlII[0:IIIllIIll]