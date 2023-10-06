import math
def IIIIIIIIIIIIIIIl(IlIIIlllllI, lIIIIIlIIlllIlI, IIlIIlIlIIIIIllIIlI, IlIlIlIlll):
  lIIlllllllllIllllIlI = IIlIIlIlIIIIIllIIlI+IlIlIlIlll
  IlIIllIIl = min(IIlIIlIlIIIIIllIIlI+2*IlIlIlIlll, len(IlIIIlllllI))
  llllIIlIllI, IIIIllIllllIIlIIlI, lIIlIlIllllllIIIlIl = IIlIIlIlIIIIIllIIlI, IIlIIlIlIIIIIllIIlI+IlIlIlIlll, IIlIIlIlIIIIIllIIlI
  while llllIIlIllI < lIIlllllllllIllllIlI and IIIIllIllllIIlIIlI < IlIIllIIl:
    if IlIIIlllllI[llllIIlIllI] < IlIIIlllllI[IIIIllIllllIIlIIlI]:
      lIIIIIlIIlllIlI[lIIlIlIllllllIIIlIl] = IlIIIlllllI[llllIIlIllI]
      llllIIlIllI += 1
    else:
      lIIIIIlIIlllIlI[lIIlIlIllllllIIIlIl] = IlIIIlllllI[IIIIllIllllIIlIIlI]
      IIIIllIllllIIlIIlI += 1
    lIIlIlIllllllIIIlIl -= 1
  if llllIIlIllI < lIIlllllllllIllllIlI:
    lIIIIIlIIlllIlI[lIIlIlIllllllIIIlIl:IlIIllIIl] = IlIIIlllllI[llllIIlIllI:lIIlllllllllIllllIlI]
  elif IIIIllIllllIIlIIlI < IlIIllIIl:
    lIIIIIlIIlllIlI[lIIlIlIllllllIIIlIl:IlIIllIIl] = IlIIIlllllI[IIIIllIllllIIlIIlI:IlIIllIIl]
def IlIIlIlIlIIIII(IllIIlIIlllIlIIl):
  IlIIIlIIIllllIllIl = len(IllIIlIIlllIlIIl)
  llIIIllIlIlIlllII = math.ceil(math.log(IlIIIlIIIllllIllIl,2))
  IlIIIlllllI, lIIllIIIlIlllllI = IllIIlIIlllIlIIl, [None] * IlIIIlIIIllllIllIl
  for IIIIllllIllIIllIIl in (2**lIllIllIlIlIlIII for lIllIllIlIlIlIII in range(llIIIllIlIlIlllII)):
    for llIIIIlllIl in range(0, IlIIIlIIIllllIllIl, 2*IIIIllllIllIIllIIl):
      IIIIIIIIIIIIIIIl(IlIIIlllllI, lIIllIIIlIlllllI, llIIIIlllIl, IIIIllllIllIIllIIl)
    IlIIIlllllI, lIIllIIIlIlllllI = lIIllIIIlIlllllI, IlIIIlllllI
  if IllIIlIIlllIlIIl is not IlIIIlllllI:
    IllIIlIIlllIlIIl[0:IlIIIlIIIllllIllIl] = IlIIIlllllI[0:IlIIIlIIIllllIllIl]