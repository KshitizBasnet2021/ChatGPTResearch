import math
def lIlIIllIIlllI(IlllIlIlllllll, IIlllIlIIIIllI, IIIlllIlllllII, IllIllIIIlIllIlIIl):
  IlIIllIIIIIllIIl = IIIlllIlllllII+IllIllIIIlIllIlIIl
  llIlIIlIIIIIllIIIIII = min(IIIlllIlllllII+2*IllIllIIIlIllIlIIl, len(IlllIlIlllllll))
  lllllIIIIIIllll, IIllIlIIIIIIlII, IllIlIIlllIIlllll = IIIlllIlllllII, IIIlllIlllllII+IllIllIIIlIllIlIIl, IIIlllIlllllII
  while lllllIIIIIIllll < IlIIllIIIIIllIIl and IIllIlIIIIIIlII < llIlIIlIIIIIllIIIIII:
    if IlllIlIlllllll[lllllIIIIIIllll] < IlllIlIlllllll[IIllIlIIIIIIlII]:
      IIlllIlIIIIllI[IllIlIIlllIIlllll] = IlllIlIlllllll[lllllIIIIIIllll]
      lllllIIIIIIllll += 1
    else:
      IIlllIlIIIIllI[IllIlIIlllIIlllll] = IlllIlIlllllll[IIllIlIIIIIIlII]
      IIllIlIIIIIIlII += 1
    IllIlIIlllIIlllll += 1
  if lllllIIIIIIllll < IlIIllIIIIIllIIl:
    IIlllIlIIIIllI[IllIlIIlllIIlllll:llIlIIlIIIIIllIIIIII] = IlllIlIlllllll[lllllIIIIIIllll:IlIIllIIIIIllIIl]
  elif IIllIlIIIIIIlII < llIlIIlIIIIIllIIIIII:
    IIlllIlIIIIllI[:llIlIIlIIIIIllIIIIII] = IlllIlIlllllll[IIllIlIIIIIIlII:llIlIIlIIIIIllIIIIII]
def IIlllIIIlIlIll(lllllIll):
  IIIlIlll = len(lllllIll)
  IIllIllIIIIII = math.ceil(math.log(IIIlIlll,2))
  IlllIlIlllllll, IIIIlIlIllllIIIIIIII = lllllIll, [None] * IIIlIlll
  for lllIlIIlIl in (2**IIlIllIIIIlll for IIlIllIIIIlll in range(IIllIllIIIIII)):
    for IIIIlIIlIIlII in range(0, IIIlIlll, 2*lllIlIIlIl):
      lIlIIllIIlllI(IlllIlIlllllll, IIIIlIlIllllIIIIIIII, IIIIlIIlIIlII, lllIlIIlIl)
    IlllIlIlllllll, IIIIlIlIllllIIIIIIII = IIIIlIlIllllIIIIIIII, IlllIlIlllllll
  if lllllIll is not IlllIlIlllllll:
    lllllIll[0:IIIlIlll] = IlllIlIlllllll[0:IIIlIlll]