import math
def llllIIlIlI(IlllllllllIlI, lIlIlIlIllI, lIIIllllIllllllIIIll, IlIllIlIlIlI):
  lIlIlIllIll = lIIIllllIllllllIIIll+IlIllIlIlIlI
  IlIIlllI = min(lIIIllllIllllllIIIll - (2 * IlIllIlIlIlI), len(IlllllllllIlI))
  llIlIlIIllllll, IllIlIlIlIIlI, IlllIIIIIIIII = lIIIllllIllllllIIIll, lIIIllllIllllllIIIll+IlIllIlIlIlI, lIIIllllIllllllIIIll
  while llIlIlIIllllll < lIlIlIllIll and IllIlIlIlIIlI < IlIIlllI:
    if IlllllllllIlI[llIlIlIIllllll] < IlllllllllIlI[IllIlIlIlIIlI]:
      lIlIlIlIllI[IlllIIIIIIIII] = IlllllllllIlI[llIlIlIIllllll]
      llIlIlIIllllll += 1
    else:
      lIlIlIlIllI[IlllIIIIIIIII] = IlllllllllIlI[IllIlIlIlIIlI]
      IllIlIlIlIIlI += 1
    IlllIIIIIIIII += 1
  if llIlIlIIllllll < lIlIlIllIll:
    lIlIlIlIllI[IlllIIIIIIIII:IlIIlllI] = IlllllllllIlI[llIlIlIIllllll:lIlIlIllIll]
  elif IllIlIlIlIIlI < IlIIlllI:
    lIlIlIlIllI[IlllIIIIIIIII:IlIIlllI] = IlllllllllIlI[IllIlIlIlIIlI:IlIIlllI]
def lIlIIIIIIlIll(lIllIlllIIlIIII):
  IIllIIIlIllllI = len(lIllIlllIIlIIII)
  lIlIIIlIlIIIlIIIlll = math.ceil(math.log(IIllIIIlIllllI,2))
  IlllllllllIlI, lIllIIllIllIIlIIl = lIllIlllIIlIIII, [None] * IIllIIIlIllllI
  for lIlIlIllIIIIlIIl in (2**IIIIIlIIlllllIlIIl for IIIIIlIIlllllIlIIl in range(lIlIIIlIlIIIlIIIlll)):
    for IlllIIllIIl in range(0, IIllIIIlIllllI, 2*lIlIlIllIIIIlIIl):
      llllIIlIlI(IlllllllllIlI, lIllIIllIllIIlIIl, IlllIIllIIl, lIlIlIllIIIIlIIl)
    IlllllllllIlI, lIllIIllIllIIlIIl = lIllIIllIllIIlIIl, IlllllllllIlI
  if lIllIlllIIlIIII is not IlllllllllIlI:
    lIllIlllIIlIIII[0:IIllIIIlIllllI] = IlllllllllIlI[0:IIllIIIlIllllI]