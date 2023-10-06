import math
def IIlIIIllI(IllIlIlIIIlI, IllIIIlIlllIIIllIlI, IIlIIllIIlllIllIl, IlIlIlIlIIIIl):
  IlIlIlIll = IIlIIllIIlllIllIl+IlIlIlIlIIIIl
  IIlllllIIIIIIllII = min(IIlIIllIIlllIllIl+2*IlIlIlIlIIIIl, len(IllIlIlIIIlI))
  IIlIIllIllllIlllllIl, IIIIIlllIlIIIIIIllII, IlIlIIIlIlllllIlI = IIlIIllIIlllIllIl, IIlIIllIIlllIllIl+IlIlIlIlIIIIl, IIlIIllIIlllIllIl
  while IIlIIllIllllIlllllIl < IlIlIlIll and IIIIIlllIlIIIIIIllII < IIlllllIIIIIIllII:
    if IllIlIlIIIlI[IIlIIllIllllIlllllIl] <= IllIlIlIIIlI[IIIIIlllIlIIIIIIllII]:
      IllIIIlIlllIIIllIlI[IlIlIIIlIlllllIlI] = IllIlIlIIIlI[IIlIIllIllllIlllllIl]
      IIlIIllIllllIlllllIl += 1
    else:
      IllIIIlIlllIIIllIlI[IlIlIIIlIlllllIlI] = IllIlIlIIIlI[IIIIIlllIlIIIIIIllII]
      IIIIIlllIlIIIIIIllII += 1
    IlIlIIIlIlllllIlI += 1
  if IIlIIllIllllIlllllIl < IlIlIlIll:
    IllIIIlIlllIIIllIlI[IlIlIIIlIlllllIlI:IIlllllIIIIIIllII] = IllIlIlIIIlI[IIlIIllIllllIlllllIl:IlIlIlIll]
  elif IIIIIlllIlIIIIIIllII < IIlllllIIIIIIllII:
    IllIIIlIlllIIIllIlI[IlIlIIIlIlllllIlI:IIlllllIIIIIIllII] = IllIlIlIIIlI[IIIIIlllIlIIIIIIllII:IIlllllIIIIIIllII]
def IIIlIIIllllllI(IlIlllIllllIl):
  lIIIlIlIll = len(IlIlllIllllIl)
  IIIIllIIIlllIl = math.ceil(math.log(lIIIlIlIll,2))
  IllIlIlIIIlI, IlIIlIllIIlIl = IlIlllIllllIl, [None] * lIIIlIlIll
  for IIlllIlIlIlIlI in (2**lIlIlIlIlIlIlll for lIlIlIlIlIlIlll in range(IIIIllIIIlllIl)):
    for IIlIlIIllIlllII in range(0, lIIIlIlIll, 2*IIlllIlIlIlIlI):
      IIlIIIllI(IllIlIlIIIlI, IlIIlIllIIlIl, IIlIlIIllIlllII, IIlllIlIlIlIlI)
    IllIlIlIIIlI, IlIIlIllIIlIl = IlIIlIllIIlIl, IllIlIlIIIlI
  if IlIlllIllllIl is not IllIlIlIIIlI:
    IlIlllIllllIl[0:lIIIlIlIll] = IllIlIlIIIlI[0:lIIIlIlIll]