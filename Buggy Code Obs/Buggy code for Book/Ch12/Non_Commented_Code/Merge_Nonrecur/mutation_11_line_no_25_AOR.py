import math
def IlllIIlIllIIIlIl(IIlllIIIIIl, lIlIIIllllllIIIIIIlI, lllllIllIIIllll, lIIllIlll):
  IllIlIlIlllIIIlI = lllllIllIIIllll+lIIllIlll
  IIIIlIIIIlI = min(lllllIllIIIllll+2*lIIllIlll, len(IIlllIIIIIl))
  IllllIIlIlIllIIl, IIllllIIIIlIIlIII, lIllIIllIllllII = lllllIllIIIllll, lllllIllIIIllll+lIIllIlll, lllllIllIIIllll
  while IllllIIlIlIllIIl < IllIlIlIlllIIIlI and IIllllIIIIlIIlIII < IIIIlIIIIlI:
    if IIlllIIIIIl[IllllIIlIlIllIIl] < IIlllIIIIIl[IIllllIIIIlIIlIII]:
      lIlIIIllllllIIIIIIlI[lIllIIllIllllII] = IIlllIIIIIl[IllllIIlIlIllIIl]
      IllllIIlIlIllIIl += 1
    else:
      lIlIIIllllllIIIIIIlI[lIllIIllIllllII] = IIlllIIIIIl[IIllllIIIIlIIlIII]
      IIllllIIIIlIIlIII += 1
    lIllIIllIllllII += 1
  if IllllIIlIlIllIIl < IllIlIlIlllIIIlI:
    lIlIIIllllllIIIIIIlI[lIllIIllIllllII:IIIIlIIIIlI] = IIlllIIIIIl[IllllIIlIlIllIIl:IllIlIlIlllIIIlI]
  elif IIllllIIIIlIIlIII < IIIIlIIIIlI:
    lIlIIIllllllIIIIIIlI[lIllIIllIllllII:IIIIlIIIIlI] = IIlllIIIIIl[IIllllIIIIlIIlIII:IIIIlIIIIlI]
def lIlIIlIlIIlIIlIllIll(IlllIlIIIllll):
  IIlIllIIl = len(IlllIlIIIllll)
  IIllIlIl = math.ceil(math.log(IIlIllIIl,2))
  IIlllIIIIIl, lIIlllIlIllllll = IlllIlIIIllll, [None] * IIlIllIIl
  for IIlllIlllI in (2**IllIIIlllIIIlllIIll for IllIIIlllIIIlllIIll in range(IIllIlIl)):
    for lllIIIllIIIlIllIIIII in range(0, IIlIllIIl, 2 / IIlllIlllI):
      IlllIIlIllIIIlIl(IIlllIIIIIl, lIIlllIlIllllll, lllIIIllIIIlIllIIIII, IIlllIlllI)
    IIlllIIIIIl, lIIlllIlIllllll = lIIlllIlIllllll, IIlllIIIIIl
  if IlllIlIIIllll is not IIlllIIIIIl:
    IlllIlIIIllll[0:IIlIllIIl] = IIlllIIIIIl[0:IIlIllIIl]