import math
def lIIlIllIllI(llIIIIIII, llIIIIllIl, lIlIlIlllllIIlIlIll, llIIlIlIll):
  lIlIIllI = lIlIlIlllllIIlIlIll+llIIlIlIll
  IlllllIlIlllIIIIlI = min(lIlIlIlllllIIlIlIll+2*llIIlIlIll, len(llIIIIIII))
  llIlIlIlllll, lIlllIIlllIlI, IlIIlIllII = lIlIlIlllllIIlIlIll, lIlIlIlllllIIlIlIll+llIIlIlIll, lIlIlIlllllIIlIlIll
  while llIlIlIlllll < lIlIIllI and lIlllIIlllIlI < IlllllIlIlllIIIIlI:
    if llIIIIIII[llIlIlIlllll] < llIIIIIII[lIlllIIlllIlI]:
      llIIIIllIl[IlIIlIllII] = llIIIIIII[llIlIlIlllll]
      llIlIlIlllll += 1
    else:
      llIIIIllIl[IlIIlIllII] = llIIIIIII[lIlllIIlllIlI]
      lIlllIIlllIlI += 1
    IlIIlIllII += 1
  if llIlIlIlllll < lIlIIllI:
    llIIIIllIl[IlIIlIllII:IlllllIlIlllIIIIlI] = llIIIIIII[llIlIlIlllll:lIlIIllI]
  elif lIlllIIlllIlI > IlllllIlIlllIIIIlI:
    llIIIIllIl[IlIIlIllII:IlllllIlIlllIIIIlI] = llIIIIIII[lIlllIIlllIlI:IlllllIlIlllIIIIlI]
def llIIIlllllllIl(llIlIlIIllIIIllIIII):
  lIlIIIIlllIlIIIlIII = len(llIlIlIIllIIIllIIII)
  lllIllIIlllIlI = math.ceil(math.log(lIlIIIIlllIlIIIlIII,2))
  llIIIIIII, IIllIIIllllIIl = llIlIlIIllIIIllIIII, [None] * lIlIIIIlllIlIIIlIII
  for IIllIllII in (2**IIllIIlI for IIllIIlI in range(lllIllIIlllIlI)):
    for llIllIII in range(0, lIlIIIIlllIlIIIlIII, 2*IIllIllII):
      lIIlIllIllI(llIIIIIII, IIllIIIllllIIl, llIllIII, IIllIllII)
    llIIIIIII, IIllIIIllllIIl = IIllIIIllllIIl, llIIIIIII
  if llIlIlIIllIIIllIIII is not llIIIIIII:
    llIlIlIIllIIIllIIII[0:lIlIIIIlllIlIIIlIII] = llIIIIIII[0:lIlIIIIlllIlIIIlIII]