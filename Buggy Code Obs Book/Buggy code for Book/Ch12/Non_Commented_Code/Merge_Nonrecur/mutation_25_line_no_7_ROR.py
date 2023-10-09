import math
def IIIIIlllIlll(lIIlIIlllIIIlIIlll, llllIIIIlIIIIlII, IlllIlIll, IllIlllIlllIlIl):
  IIIIlIlI = IlllIlIll+IllIlllIlllIlIl
  IIllIIlIlllI = min(IlllIlIll+2*IllIlllIlllIlIl, len(lIIlIIlllIIIlIIlll))
  IIlIlIIIlIllIlllllll, IIIlIlIIlIlIlllI, IlIllIlII = IlllIlIll, IlllIlIll+IllIlllIlllIlIl, IlllIlIll
  while (IIlIlIIIlIllIlllllll < IIIIlIlI and IIIlIlIIlIlIlllI > IIllIIlIlllI):
    if lIIlIIlllIIIlIIlll[IIlIlIIIlIllIlllllll] < lIIlIIlllIIIlIIlll[IIIlIlIIlIlIlllI]:
      llllIIIIlIIIIlII[IlIllIlII] = lIIlIIlllIIIlIIlll[IIlIlIIIlIllIlllllll]
      IIlIlIIIlIllIlllllll += 1
    else:
      llllIIIIlIIIIlII[IlIllIlII] = lIIlIIlllIIIlIIlll[IIIlIlIIlIlIlllI]
      IIIlIlIIlIlIlllI += 1
    IlIllIlII += 1
  if IIlIlIIIlIllIlllllll < IIIIlIlI:
    llllIIIIlIIIIlII[IlIllIlII:IIllIIlIlllI] = lIIlIIlllIIIlIIlll[IIlIlIIIlIllIlllllll:IIIIlIlI]
  elif IIIlIlIIlIlIlllI < IIllIIlIlllI:
    llllIIIIlIIIIlII[IlIllIlII:IIllIIlIlllI] = lIIlIIlllIIIlIIlll[IIIlIlIIlIlIlllI:IIllIIlIlllI]
def lIIllIlIIIlIIIl(lllllIlIIIlIIlll):
  IllIIIIlIlllIIlIIl = len(lllllIlIIIlIIlll)
  lIllIllIIlIIIIIl = math.ceil(math.log(IllIIIIlIlllIIlIIl,2))
  lIIlIIlllIIIlIIlll, IIllllll = lllllIlIIIlIIlll, [None] * IllIIIIlIlllIIlIIl
  for IlIIlIlIlIIIlIIIl in (2**lllIlIllIIIlIl for lllIlIllIIIlIl in range(lIllIllIIlIIIIIl)):
    for lIIllIllIlllI in range(0, IllIIIIlIlllIIlIIl, 2*IlIIlIlIlIIIlIIIl):
      IIIIIlllIlll(lIIlIIlllIIIlIIlll, IIllllll, lIIllIllIlllI, IlIIlIlIlIIIlIIIl)
    lIIlIIlllIIIlIIlll, IIllllll = IIllllll, lIIlIIlllIIIlIIlll
  if lllllIlIIIlIIlll is not lIIlIIlllIIIlIIlll:
    lllllIlIIIlIIlll[0:IllIIIIlIlllIIlIIl] = lIIlIIlllIIIlIIlll[0:IllIIIIlIlllIIlIIl]