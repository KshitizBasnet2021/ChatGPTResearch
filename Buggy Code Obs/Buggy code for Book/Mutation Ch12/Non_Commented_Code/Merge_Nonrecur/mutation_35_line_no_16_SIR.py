import math
def IlIllIlIIIllI(IIIIIlllllll, lIlIIllllIlIllllIIIl, lllIIllIlIIIIlll, IlIlIIllIllIllIII):
  IIIlllIllllIIIllll = lllIIllIlIIIIlll+IlIlIIllIllIllIII
  IllIllllIlI = min(lllIIllIlIIIIlll+2*IlIlIIllIllIllIII, len(IIIIIlllllll))
  lIlIlllIlIllIIIlIII, IlIllIlIIIllIllII, IIIllIIIII = lllIIllIlIIIIlll, lllIIllIlIIIIlll+IlIlIIllIllIllIII, lllIIllIlIIIIlll
  while lIlIlllIlIllIIIlIII < IIIlllIllllIIIllll and IlIllIlIIIllIllII < IllIllllIlI:
    if IIIIIlllllll[lIlIlllIlIllIIIlIII] < IIIIIlllllll[IlIllIlIIIllIllII]:
      lIlIIllllIlIllllIIIl[IIIllIIIII] = IIIIIlllllll[lIlIlllIlIllIIIlIII]
      lIlIlllIlIllIIIlIII += 1
    else:
      lIlIIllllIlIllllIIIl[IIIllIIIII] = IIIIIlllllll[IlIllIlIIIllIllII]
      IlIllIlIIIllIllII += 1
    IIIllIIIII += 1
  if lIlIlllIlIllIIIlIII < IIIlllIllllIIIllll:
    lIlIIllllIlIllllIIIl[IIIllIIIII:IllIllllIlI] = IIIIIlllllll[:IIIlllIllllIIIllll]
  elif IlIllIlIIIllIllII < IllIllllIlI:
    lIlIIllllIlIllllIIIl[IIIllIIIII:IllIllllIlI] = IIIIIlllllll[IlIllIlIIIllIllII:IllIllllIlI]
def lllIIIllllllIIIl(IlIllIIIIIlIIIIIIl):
  IIIlIllIIIlI = len(IlIllIIIIIlIIIIIIl)
  IllIlIllIIIllIIllI = math.ceil(math.log(IIIlIllIIIlI,2))
  IIIIIlllllll, IlllIIll = IlIllIIIIIlIIIIIIl, [None] * IIIlIllIIIlI
  for lIIIlllIII in (2**lllIIIlIIIIlll for lllIIIlIIIIlll in range(IllIlIllIIIllIIllI)):
    for lllIlIlIIl in range(0, IIIlIllIIIlI, 2*lIIIlllIII):
      IlIllIlIIIllI(IIIIIlllllll, IlllIIll, lllIlIlIIl, lIIIlllIII)
    IIIIIlllllll, IlllIIll = IlllIIll, IIIIIlllllll
  if IlIllIIIIIlIIIIIIl is not IIIIIlllllll:
    IlIllIIIIIlIIIIIIl[0:IIIlIllIIIlI] = IIIIIlllllll[0:IIIlIllIIIlI]