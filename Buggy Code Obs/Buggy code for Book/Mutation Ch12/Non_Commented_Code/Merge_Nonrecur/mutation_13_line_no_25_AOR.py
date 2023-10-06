import math
def IllllIlIIlIIlIl(IllllIIIIIlIllIlIII, lllIIIlI, lllIlIlllIlIIllIIll, llllIlIIlIllll):
  lIIIIIllIIIllIlIIIlI = lllIlIlllIlIIllIIll+llllIlIIlIllll
  lIlllIllIllIIllI = min(lllIlIlllIlIIllIIll+2*llllIlIIlIllll, len(IllllIIIIIlIllIlIII))
  IIlIIIIllllIIIlIIIll, llIllIlIlllIlIIIIlIl, llIIlllIIllI = lllIlIlllIlIIllIIll, lllIlIlllIlIIllIIll+llllIlIIlIllll, lllIlIlllIlIIllIIll
  while IIlIIIIllllIIIlIIIll < lIIIIIllIIIllIlIIIlI and llIllIlIlllIlIIIIlIl < lIlllIllIllIIllI:
    if IllllIIIIIlIllIlIII[IIlIIIIllllIIIlIIIll] < IllllIIIIIlIllIlIII[llIllIlIlllIlIIIIlIl]:
      lllIIIlI[llIIlllIIllI] = IllllIIIIIlIllIlIII[IIlIIIIllllIIIlIIIll]
      IIlIIIIllllIIIlIIIll += 1
    else:
      lllIIIlI[llIIlllIIllI] = IllllIIIIIlIllIlIII[llIllIlIlllIlIIIIlIl]
      llIllIlIlllIlIIIIlIl += 1
    llIIlllIIllI += 1
  if IIlIIIIllllIIIlIIIll < lIIIIIllIIIllIlIIIlI:
    lllIIIlI[llIIlllIIllI:lIlllIllIllIIllI] = IllllIIIIIlIllIlIII[IIlIIIIllllIIIlIIIll:lIIIIIllIIIllIlIIIlI]
  elif llIllIlIlllIlIIIIlIl < lIlllIllIllIIllI:
    lllIIIlI[llIIlllIIllI:lIlllIllIllIIllI] = IllllIIIIIlIllIlIII[llIllIlIlllIlIIIIlIl:lIlllIllIllIIllI]
def IllIllIlIIlIll(llIlIIlI):
  IIIlIllI = len(llIlIIlI)
  lIIIlIllI = math.ceil(math.log(IIIlIllI,2))
  IllllIIIIIlIllIlIII, IIlIIIIIIIIlIlIIlIlI = llIlIIlI, [None] * IIIlIllI
  for lIIlIIIllIlllllIl in (2**lIlIlllIIIIIIl for lIlIlllIIIIIIl in range(lIIIlIllI)):
    for IlIllIlIlllIlIlll in range(0, IIIlIllI, 2 ** lIIlIIIllIlllllIl):
      IllllIlIIlIIlIl(IllllIIIIIlIllIlIII, IIlIIIIIIIIlIlIIlIlI, IlIllIlIlllIlIlll, lIIlIIIllIlllllIl)
    IllllIIIIIlIllIlIII, IIlIIIIIIIIlIlIIlIlI = IIlIIIIIIIIlIlIIlIlI, IllllIIIIIlIllIlIII
  if llIlIIlI is not IllllIIIIIlIllIlIII:
    llIlIIlI[0:IIIlIllI] = IllllIIIIIlIllIlIII[0:IIIlIllI]