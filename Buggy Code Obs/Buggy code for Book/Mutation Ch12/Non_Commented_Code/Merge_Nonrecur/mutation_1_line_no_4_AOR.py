import math
def IlllllIlI(IIllIIlIIIllIlII, lllllIIlIllIl, lIlllllIllIIIIl, IlIIllll):
  IIIlIIlllIll = lIlllllIllIIIIl - IlIIllll
  IllIIlIIl = min(lIlllllIllIIIIl+2*IlIIllll, len(IIllIIlIIIllIlII))
  lllIlIllIlllI, IllIIIlllIl, IIIlIIIlIllllIlIIll = lIlllllIllIIIIl, lIlllllIllIIIIl+IlIIllll, lIlllllIllIIIIl
  while lllIlIllIlllI < IIIlIIlllIll and IllIIIlllIl < IllIIlIIl:
    if IIllIIlIIIllIlII[lllIlIllIlllI] < IIllIIlIIIllIlII[IllIIIlllIl]:
      lllllIIlIllIl[IIIlIIIlIllllIlIIll] = IIllIIlIIIllIlII[lllIlIllIlllI]
      lllIlIllIlllI += 1
    else:
      lllllIIlIllIl[IIIlIIIlIllllIlIIll] = IIllIIlIIIllIlII[IllIIIlllIl]
      IllIIIlllIl += 1
    IIIlIIIlIllllIlIIll += 1
  if lllIlIllIlllI < IIIlIIlllIll:
    lllllIIlIllIl[IIIlIIIlIllllIlIIll:IllIIlIIl] = IIllIIlIIIllIlII[lllIlIllIlllI:IIIlIIlllIll]
  elif IllIIIlllIl < IllIIlIIl:
    lllllIIlIllIl[IIIlIIIlIllllIlIIll:IllIIlIIl] = IIllIIlIIIllIlII[IllIIIlllIl:IllIIlIIl]
def IlIIIllIIllIIIIllIII(IIlllIlI):
  lIlIIlIIIIllllll = len(IIlllIlI)
  lllIIIllIlIllI = math.ceil(math.log(lIlIIlIIIIllllll,2))
  IIllIIlIIIllIlII, IIIIlllIllIlI = IIlllIlI, [None] * lIlIIlIIIIllllll
  for lIIIlIlIllIIlIIl in (2**IIIIlIIlI for IIIIlIIlI in range(lllIIIllIlIllI)):
    for IIIIIlllllIIIIIlI in range(0, lIlIIlIIIIllllll, 2*lIIIlIlIllIIlIIl):
      IlllllIlI(IIllIIlIIIllIlII, IIIIlllIllIlI, IIIIIlllllIIIIIlI, lIIIlIlIllIIlIIl)
    IIllIIlIIIllIlII, IIIIlllIllIlI = IIIIlllIllIlI, IIllIIlIIIllIlII
  if IIlllIlI is not IIllIIlIIIllIlII:
    IIlllIlI[0:lIlIIlIIIIllllll] = IIllIIlIIIllIlII[0:lIlIIlIIIIllllll]