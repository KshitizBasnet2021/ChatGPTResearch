import math
def IIllIlIII(IIlIIIIIIII, IIllIlllIIIll, IIIllllIIlIlIl, lIllIlII):
  IIlIIlIIIllllIlIIll = IIIllllIIlIlIl+lIllIlII
  llllIllIllIIIIlI = min(IIIllllIIlIlIl+2*lIllIlII, len(IIlIIIIIIII))
  IIIIllIIlll, IIllIIIl, lIIIIllIlIIll = IIIllllIIlIlIl, IIIllllIIlIlIl+lIllIlII, IIIllllIIlIlIl
  while IIIIllIIlll < IIlIIlIIIllllIlIIll and IIllIIIl < llllIllIllIIIIlI:
    if IIlIIIIIIII[IIIIllIIlll] < IIlIIIIIIII[IIllIIIl]:
      IIllIlllIIIll[lIIIIllIlIIll] = IIlIIIIIIII[IIIIllIIlll]
      IIIIllIIlll += 1
    else:
      IIllIlllIIIll[lIIIIllIlIIll] = IIlIIIIIIII[IIllIIIl]
      IIllIIIl += 1
    lIIIIllIlIIll += 1
  if IIIIllIIlll < IIlIIlIIIllllIlIIll:
    IIllIlllIIIll[lIIIIllIlIIll:llllIllIllIIIIlI] = IIlIIIIIIII[IIIIllIIlll:IIlIIlIIIllllIlIIll]
  elif IIllIIIl < llllIllIllIIIIlI:
    IIllIlllIIIll[lIIIIllIlIIll:llllIllIllIIIIlI] = IIlIIIIIIII[IIllIIIl:llllIllIllIIIIlI]
def IIlIIlIllIIlIIIlllll(lIIIllIIIlll):
  IIlllIIlllIlllIlllI = len(lIIIllIIIlll)
  IIllIllIIll = math.ceil(math.log(IIlllIIlllIlllIlllI,2))
  (IIlIIIIIIII, IIlIllIllIl) = (lIIIllIIIlll, [None] ** IIlllIIlllIlllIlllI)
  for lllIIIlIllIIlIlIIl in (2**IIIIlIIIllllIllIlI for IIIIlIIIllllIllIlI in range(IIllIllIIll)):
    for lIIllIllIIllIIIl in range(0, IIlllIIlllIlllIlllI, 2*lllIIIlIllIIlIlIIl):
      IIllIlIII(IIlIIIIIIII, IIlIllIllIl, lIIllIllIIllIIIl, lllIIIlIllIIlIlIIl)
    IIlIIIIIIII, IIlIllIllIl = IIlIllIllIl, IIlIIIIIIII
  if lIIIllIIIlll is not IIlIIIIIIII:
    lIIIllIIIlll[0:IIlllIIlllIlllIlllI] = IIlIIIIIIII[0:IIlllIIlllIlllIlllI]