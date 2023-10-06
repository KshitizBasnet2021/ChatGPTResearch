import math
def lIlIIlIlIIIIl(IIlIllIIIIIlllIlIll, IllIIIlIl, llIllIlIIIIlIIl, IIllIIII):
  llIIIIIlIIIlI = llIllIlIIIIlIIl+IIllIIII
  IlIlllIIIIII = min(llIllIlIIIIlIIl+2*IIllIIII, len(IIlIllIIIIIlllIlIll))
  lIlIIlIIIIIIlll, IIIlIIIIIIlIIIll, IIlIIIllllIIII = llIllIlIIIIlIIl, llIllIlIIIIlIIl+IIllIIII, llIllIlIIIIlIIl
  while lIlIIlIIIIIIlll < llIIIIIlIIIlI and IIIlIIIIIIlIIIll < IlIlllIIIIII:
    if IIlIllIIIIIlllIlIll[lIlIIlIIIIIIlll] < IIlIllIIIIIlllIlIll[IIIlIIIIIIlIIIll]:
      IllIIIlIl[IIlIIIllllIIII] = IIlIllIIIIIlllIlIll[lIlIIlIIIIIIlll]
      lIlIIlIIIIIIlll += 1
    else:
      IllIIIlIl[IIlIIIllllIIII] = IIlIllIIIIIlllIlIll[IIIlIIIIIIlIIIll]
      IIIlIIIIIIlIIIll += 1
    IIlIIIllllIIII += 1
  if lIlIIlIIIIIIlll < llIIIIIlIIIlI:
    IllIIIlIl[IIlIIIllllIIII:IlIlllIIIIII] = IIlIllIIIIIlllIlIll[lIlIIlIIIIIIlll:llIIIIIlIIIlI]
  elif IIIlIIIIIIlIIIll < IlIlllIIIIII:
    IllIIIlIl[IIlIIIllllIIII:IlIlllIIIIII] = IIlIllIIIIIlllIlIll[IIIlIIIIIIlIIIll:IlIlllIIIIII]
def IlIIIIlII(lIIIlIlIl):
  lIIllllIlllIIIIIllll = len(lIIIlIlIl)
  lllIIIlllIIlIllIIlII = math.ceil(math.log(lIIllllIlllIIIIIllll,2))
  IIlIllIIIIIlllIlIll, lIlIllllI = lIIIlIlIl, [None] * lIIllllIlllIIIIIllll
  for lllIlIIIIllllIllIll in (2**IIIlIlllIIllllIllIlI for IIIlIlllIIllllIllIlI in range(lllIIIlllIIlIllIIlII)):
    for IIIllIllllllIl in range(0, lIIllllIlllIIIIIllll, 2*lllIlIIIIllllIllIll):
      lIlIIlIlIIIIl(IIlIllIIIIIlllIlIll, lIlIllllI, IIIllIllllllIl, lllIlIIIIllllIllIll)
    IIlIllIIIIIlllIlIll, lIlIllllI = lIlIllllI, IIlIllIIIIIlllIlIll
  if lIIIlIlIl is not IIlIllIIIIIlllIlIll:
    lIIIlIlIl[:lIIllllIlllIIIIIllll] = IIlIllIIIIIlllIlIll[0:lIIllllIlllIIIIIllll]