import math
def IlIlIlllllll(IIIllllI, IIIIlIlIIIlllI, IIlIlIlllIIIllllll, llIllIllI):
  IllIIllllIllIllIllIl = IIlIlIlllIIIllllll+llIllIllI
  IlIIIIIIIIIIlIII = min(IIlIlIlllIIIllllll+2*llIllIllI, len(IIIllllI))
  IlIlIllllIlIll, IlllllIllllIIIllIlll, llIIllIllllIIlIIl = IIlIlIlllIIIllllll, IIlIlIlllIIIllllll+llIllIllI, IIlIlIlllIIIllllll
  while IlIlIllllIlIll < IllIIllllIllIllIllIl and IlllllIllllIIIllIlll < IlIIIIIIIIIIlIII:
    if IIIllllI[IlIlIllllIlIll] < IIIllllI[IlllllIllllIIIllIlll]:
      IIIIlIlIIIlllI[llIIllIllllIIlIIl] = IIIllllI[IlIlIllllIlIll]
      IlIlIllllIlIll += 1
    else:
      IIIIlIlIIIlllI[llIIllIllllIIlIIl] = IIIllllI[IlllllIllllIIIllIlll]
      IlllllIllllIIIllIlll += 1
    llIIllIllllIIlIIl += 1
  if IlIlIllllIlIll < IllIIllllIllIllIllIl:
    IIIIlIlIIIlllI[llIIllIllllIIlIIl:IlIIIIIIIIIIlIII] = IIIllllI[IlIlIllllIlIll:IllIIllllIllIllIllIl]
  elif IlllllIllllIIIllIlll < IlIIIIIIIIIIlIII:
    IIIIlIlIIIlllI[llIIllIllllIIlIIl:IlIIIIIIIIIIlIII] = IIIllllI[:IlIIIIIIIIIIlIII]
def lllllllIllIllIlII(IIlIlIIllIlIIlIllll):
  IIlIIlIIlI = len(IIlIlIIllIlIIlIllll)
  lllIIlIIII = math.ceil(math.log(IIlIIlIIlI,2))
  IIIllllI, IlIlIIllI = IIlIlIIllIlIIlIllll, [None] * IIlIIlIIlI
  for lllIIlIIll in (2**llIIIlIIII for llIIIlIIII in range(lllIIlIIII)):
    for lIlIIIIIIlllIIIlIIll in range(0, IIlIIlIIlI, 2*lllIIlIIll):
      IlIlIlllllll(IIIllllI, IlIlIIllI, lIlIIIIIIlllIIIlIIll, lllIIlIIll)
    IIIllllI, IlIlIIllI = IlIlIIllI, IIIllllI
  if IIlIlIIllIlIIlIllll is not IIIllllI:
    IIlIlIIllIlIIlIllll[0:IIlIIlIIlI] = IIIllllI[0:IIlIIlIIlI]