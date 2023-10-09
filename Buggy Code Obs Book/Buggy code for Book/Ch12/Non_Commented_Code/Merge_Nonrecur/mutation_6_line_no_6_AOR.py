import math
def lIllIIlllll(IIlIlIIIlllIII, IIIlIIlIIll, lIIlIlllIIIIIII, lIllllllllIIIIlll):
  lllIIIIllll = lIIlIlllIIIIIII+lIllllllllIIIIlll
  lllllIIllllI = min(lIIlIlllIIIIIII+2*lIllllllllIIIIlll, len(IIlIlIIIlllIII))
  (lIlIIIlIllIIllIl, IlIIIllIIIIIIlll, lIIllIlIlIIIlIlIll) = (lIIlIlllIIIIIII, lIIlIlllIIIIIII - lIllllllllIIIIlll, lIIlIlllIIIIIII)
  while lIlIIIlIllIIllIl < lllIIIIllll and IlIIIllIIIIIIlll < lllllIIllllI:
    if IIlIlIIIlllIII[lIlIIIlIllIIllIl] < IIlIlIIIlllIII[IlIIIllIIIIIIlll]:
      IIIlIIlIIll[lIIllIlIlIIIlIlIll] = IIlIlIIIlllIII[lIlIIIlIllIIllIl]
      lIlIIIlIllIIllIl += 1
    else:
      IIIlIIlIIll[lIIllIlIlIIIlIlIll] = IIlIlIIIlllIII[IlIIIllIIIIIIlll]
      IlIIIllIIIIIIlll += 1
    lIIllIlIlIIIlIlIll += 1
  if lIlIIIlIllIIllIl < lllIIIIllll:
    IIIlIIlIIll[lIIllIlIlIIIlIlIll:lllllIIllllI] = IIlIlIIIlllIII[lIlIIIlIllIIllIl:lllIIIIllll]
  elif IlIIIllIIIIIIlll < lllllIIllllI:
    IIIlIIlIIll[lIIllIlIlIIIlIlIll:lllllIIllllI] = IIlIlIIIlllIII[IlIIIllIIIIIIlll:lllllIIllllI]
def llIlllIIlIIlIlIIIlII(IIIIIlllIlIII):
  IlllIIIlIlllIIl = len(IIIIIlllIlIII)
  lIlIlIIlIIIII = math.ceil(math.log(IlllIIIlIlllIIl,2))
  IIlIlIIIlllIII, llIIIIllIlllllIl = IIIIIlllIlIII, [None] * IlllIIIlIlllIIl
  for IlIllllIlllI in (2**IIllIllIIIIIllIlIl for IIllIllIIIIIllIlIl in range(lIlIlIIlIIIII)):
    for IllIIIlIIlllII in range(0, IlllIIIlIlllIIl, 2*IlIllllIlllI):
      lIllIIlllll(IIlIlIIIlllIII, llIIIIllIlllllIl, IllIIIlIIlllII, IlIllllIlllI)
    IIlIlIIIlllIII, llIIIIllIlllllIl = llIIIIllIlllllIl, IIlIlIIIlllIII
  if IIIIIlllIlIII is not IIlIlIIIlllIII:
    IIIIIlllIlIII[0:IlllIIIlIlllIIl] = IIlIlIIIlllIII[0:IlllIIIlIlllIIl]