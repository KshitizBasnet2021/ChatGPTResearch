import math
def lIIllIIIlIIIIIlII(IlIIIIlllIIl, IllIIlllIIIIll, IlllIlIlIllIllIIIIll, lIIIlIlIIlIIllIl):
  llIIIllIlIlIlllIIlII = IlllIlIlIllIllIIIIll+lIIIlIlIIlIIllIl
  IlIllllII = min(IlllIlIlIllIllIIIIll+2*lIIIlIlIIlIIllIl, len(IlIIIIlllIIl))
  IllIlIIIlllIIlllllll, IIlIlIlIIlIlII, llIllIllIlllllIlI = IlllIlIlIllIllIIIIll, IlllIlIlIllIllIIIIll+lIIIlIlIIlIIllIl, IlllIlIlIllIllIIIIll
  while IllIlIIIlllIIlllllll < llIIIllIlIlIlllIIlII and IIlIlIlIIlIlII < IlIllllII:
    if IlIIIIlllIIl[IllIlIIIlllIIlllllll] > IlIIIIlllIIl[IIlIlIlIIlIlII]:
      IllIIlllIIIIll[llIllIllIlllllIlI] = IlIIIIlllIIl[IllIlIIIlllIIlllllll]
      IllIlIIIlllIIlllllll += 1
    else:
      IllIIlllIIIIll[llIllIllIlllllIlI] = IlIIIIlllIIl[IIlIlIlIIlIlII]
      IIlIlIlIIlIlII += 1
    llIllIllIlllllIlI += 1
  if IllIlIIIlllIIlllllll < llIIIllIlIlIlllIIlII:
    IllIIlllIIIIll[llIllIllIlllllIlI:IlIllllII] = IlIIIIlllIIl[IllIlIIIlllIIlllllll:llIIIllIlIlIlllIIlII]
  elif IIlIlIlIIlIlII < IlIllllII:
    IllIIlllIIIIll[llIllIllIlllllIlI:IlIllllII] = IlIIIIlllIIl[IIlIlIlIIlIlII:IlIllllII]
def IIIIlIllIllIII(lllIllllIIIIIlIlllI):
  IllllIllIlI = len(lllIllllIIIIIlIlllI)
  lIllIIllIIIIlIlIIll = math.ceil(math.log(IllllIllIlI,2))
  IlIIIIlllIIl, IllIIlIIIII = lllIllllIIIIIlIlllI, [None] * IllllIllIlI
  for IlllIlIIllIlllIIlII in (2**IlllllIIlIII for IlllllIIlIII in range(lIllIIllIIIIlIlIIll)):
    for IIllIlllIIIIllIll in range(0, IllllIllIlI, 2*IlllIlIIllIlllIIlII):
      lIIllIIIlIIIIIlII(IlIIIIlllIIl, IllIIlIIIII, IIllIlllIIIIllIll, IlllIlIIllIlllIIlII)
    IlIIIIlllIIl, IllIIlIIIII = IllIIlIIIII, IlIIIIlllIIl
  if lllIllllIIIIIlIlllI is not IlIIIIlllIIl:
    lllIllllIIIIIlIlllI[0:IllllIllIlI] = IlIIIIlllIIl[0:IllllIllIlI]