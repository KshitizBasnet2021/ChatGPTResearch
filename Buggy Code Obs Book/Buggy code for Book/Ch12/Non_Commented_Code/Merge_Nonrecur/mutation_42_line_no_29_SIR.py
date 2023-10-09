import math
def IIlllIIllIIlIlIlIl(IllllIIIIIIIIIIl, IIIIIlll, IlIIIIII, IIIIIIIlI):
  IlllllIIIIIIIlIIlll = IlIIIIII+IIIIIIIlI
  llIIllIIIIllll = min(IlIIIIII+2*IIIIIIIlI, len(IllllIIIIIIIIIIl))
  lIIlIlIlIIIll, IIlIlIlIIlIlIIlIIIIl, lIlIIIlIlIll = IlIIIIII, IlIIIIII+IIIIIIIlI, IlIIIIII
  while lIIlIlIlIIIll < IlllllIIIIIIIlIIlll and IIlIlIlIIlIlIIlIIIIl < llIIllIIIIllll:
    if IllllIIIIIIIIIIl[lIIlIlIlIIIll] < IllllIIIIIIIIIIl[IIlIlIlIIlIlIIlIIIIl]:
      IIIIIlll[lIlIIIlIlIll] = IllllIIIIIIIIIIl[lIIlIlIlIIIll]
      lIIlIlIlIIIll += 1
    else:
      IIIIIlll[lIlIIIlIlIll] = IllllIIIIIIIIIIl[IIlIlIlIIlIlIIlIIIIl]
      IIlIlIlIIlIlIIlIIIIl += 1
    lIlIIIlIlIll += 1
  if lIIlIlIlIIIll < IlllllIIIIIIIlIIlll:
    IIIIIlll[lIlIIIlIlIll:llIIllIIIIllll] = IllllIIIIIIIIIIl[lIIlIlIlIIIll:IlllllIIIIIIIlIIlll]
  elif IIlIlIlIIlIlIIlIIIIl < llIIllIIIIllll:
    IIIIIlll[lIlIIIlIlIll:llIIllIIIIllll] = IllllIIIIIIIIIIl[IIlIlIlIIlIlIIlIIIIl:llIIllIIIIllll]
def IlllIIIllll(llllIIIIIlIIIIIlI):
  lllIIllIIIllIIIllI = len(llllIIIIIlIIIIIlI)
  lIlIlIllllIll = math.ceil(math.log(lllIIllIIIllIIIllI,2))
  IllllIIIIIIIIIIl, IIIIlIIlllIIlIIlIl = llllIIIIIlIIIIIlI, [None] * lllIIllIIIllIIIllI
  for IlIIIIIIlI in (2**llIIIIIllIIlI for llIIIIIllIIlI in range(lIlIlIllllIll)):
    for IlIIIlIlIIIlIlllII in range(0, lllIIllIIIllIIIllI, 2*IlIIIIIIlI):
      IIlllIIllIIlIlIlIl(IllllIIIIIIIIIIl, IIIIlIIlllIIlIIlIl, IlIIIlIlIIIlIlllII, IlIIIIIIlI)
    IllllIIIIIIIIIIl, IIIIlIIlllIIlIIlIl = IIIIlIIlllIIlIIlIl, IllllIIIIIIIIIIl
  if llllIIIIIlIIIIIlI is not IllllIIIIIIIIIIl:
    llllIIIIIlIIIIIlI[0:] = IllllIIIIIIIIIIl[0:lllIIllIIIllIIIllI]