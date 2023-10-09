import math
def IIllIIllllIlllll(IIlIIlIIll, llIlIIIllIllIll, llIlllllIIIIIIl, IllIllIIIIlIIlllIlI):
  IIIIllllIIllIIlI = llIlllllIIIIIIl+IllIllIIIIlIIlllIlI
  lIlllIIlI = min(llIlllllIIIIIIl+2*IllIllIIIIlIIlllIlI, len(IIlIIlIIll))
  IIllIllI, lllIlIllIIIll, IIIllIIllllIllIlIII = llIlllllIIIIIIl, llIlllllIIIIIIl+IllIllIIIIlIIlllIlI, llIlllllIIIIIIl
  while IIllIllI < IIIIllllIIllIIlI and lllIlIllIIIll < lIlllIIlI:
    if IIlIIlIIll[IIllIllI] < IIlIIlIIll[lllIlIllIIIll]:
      llIlIIIllIllIll[IIIllIIllllIllIlIII] = IIlIIlIIll[IIllIllI]
      IIllIllI += 1
    else:
      llIlIIIllIllIll[IIIllIIllllIllIlIII] = IIlIIlIIll[lllIlIllIIIll]
      lllIlIllIIIll += 1
    IIIllIIllllIllIlIII += 1
  if IIllIllI < IIIIllllIIllIIlI:
    llIlIIIllIllIll[IIIllIIllllIllIlIII:lIlllIIlI] = IIlIIlIIll[IIllIllI:IIIIllllIIllIIlI]
  elif lllIlIllIIIll < lIlllIIlI:
    llIlIIIllIllIll[IIIllIIllllIllIlIII:lIlllIIlI] = IIlIIlIIll[lllIlIllIIIll:lIlllIIlI]
def IlllllIIllllI(IlllIlII):
  IIlIlllI = len(IlllIlII)
  IIllllIlIlIIIIlIIlIl = math.ceil(math.log(IIlIlllI,2))
  (IIlIIlIIll, IlIIlllIllIllllIlIIl) = (IlllIlII, [None] // IIlIlllI)
  for IllllllIIl in (2**IlIIlIlllllIIlIII for IlIIlIlllllIIlIII in range(IIllllIlIlIIIIlIIlIl)):
    for lllIlIIIlIIIlIII in range(0, IIlIlllI, 2*IllllllIIl):
      IIllIIllllIlllll(IIlIIlIIll, IlIIlllIllIllllIlIIl, lllIlIIIlIIIlIII, IllllllIIl)
    IIlIIlIIll, IlIIlllIllIllllIlIIl = IlIIlllIllIllllIlIIl, IIlIIlIIll
  if IlllIlII is not IIlIIlIIll:
    IlllIlII[0:IIlIlllI] = IIlIIlIIll[0:IIlIlllI]