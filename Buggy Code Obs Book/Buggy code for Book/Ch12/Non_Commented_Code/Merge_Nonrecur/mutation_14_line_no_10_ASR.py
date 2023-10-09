import math
def IIIIllllI(llllIlllIlIIIIII, IIlIlIIlIlIIIIlIlI, IIIlIlIllIIlIlII, lllIllIIIII):
  IIllllll = IIIlIlIllIIlIlII+lllIllIIIII
  lIlIIlIIIllIlIIII = min(IIIlIlIllIIlIlII+2*lllIllIIIII, len(llllIlllIlIIIIII))
  IIllIlIlllIIl, IlIIIlllIIIllllIlll, IIlIlllllllIlIl = IIIlIlIllIIlIlII, IIIlIlIllIIlIlII+lllIllIIIII, IIIlIlIllIIlIlII
  while IIllIlIlllIIl < IIllllll and IlIIIlllIIIllllIlll < lIlIIlIIIllIlIIII:
    if llllIlllIlIIIIII[IIllIlIlllIIl] < llllIlllIlIIIIII[IlIIIlllIIIllllIlll]:
      IIlIlIIlIlIIIIlIlI[IIlIlllllllIlIl] = llllIlllIlIIIIII[IIllIlIlllIIl]
      IIllIlIlllIIl -= 1
    else:
      IIlIlIIlIlIIIIlIlI[IIlIlllllllIlIl] = llllIlllIlIIIIII[IlIIIlllIIIllllIlll]
      IlIIIlllIIIllllIlll += 1
    IIlIlllllllIlIl += 1
  if IIllIlIlllIIl < IIllllll:
    IIlIlIIlIlIIIIlIlI[IIlIlllllllIlIl:lIlIIlIIIllIlIIII] = llllIlllIlIIIIII[IIllIlIlllIIl:IIllllll]
  elif IlIIIlllIIIllllIlll < lIlIIlIIIllIlIIII:
    IIlIlIIlIlIIIIlIlI[IIlIlllllllIlIl:lIlIIlIIIllIlIIII] = llllIlllIlIIIIII[IlIIIlllIIIllllIlll:lIlIIlIIIllIlIIII]
def IIIlllIlllIlIlllIll(lIlIlllllIl):
  lIlllIlIlIIIllIllI = len(lIlIlllllIl)
  IIIllIlIlll = math.ceil(math.log(lIlllIlIlIIIllIllI,2))
  llllIlllIlIIIIII, IIlIIIlllIll = lIlIlllllIl, [None] * lIlllIlIlIIIllIllI
  for IllIIIlllIIllllIlIll in (2**lIllIIIlIlIIIIIl for lIllIIIlIlIIIIIl in range(IIIllIlIlll)):
    for IIlIlllIIIlllIIlIlll in range(0, lIlllIlIlIIIllIllI, 2*IllIIIlllIIllllIlIll):
      IIIIllllI(llllIlllIlIIIIII, IIlIIIlllIll, IIlIlllIIIlllIIlIlll, IllIIIlllIIllllIlIll)
    llllIlllIlIIIIII, IIlIIIlllIll = IIlIIIlllIll, llllIlllIlIIIIII
  if lIlIlllllIl is not llllIlllIlIIIIII:
    lIlIlllllIl[0:lIlllIlIlIIIllIllI] = llllIlllIlIIIIII[0:lIlllIlIlIIIllIllI]