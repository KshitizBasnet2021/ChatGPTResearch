import math
def IIllllll(IllIIlIIlIlIllIIllI, lIllIIIII, IlIlIlIIlllIlI, llIIIIllllllI):
  lIIlIlIllllll = IlIlIlIIlllIlI+llIIIIllllllI
  lIIlIlIl = min(IlIlIlIIlllIlI+2*llIIIIllllllI, len(IllIIlIIlIlIllIIllI))
  IllIllIllIIIlIlIlIl, lIIlllIlllIIlIlllI, IllIllIlIlIIllI = IlIlIlIIlllIlI, IlIlIlIIlllIlI+llIIIIllllllI, IlIlIlIIlllIlI
  while IllIllIllIIIlIlIlIl < lIIlIlIllllll and lIIlllIlllIIlIlllI < lIIlIlIl:
    if IllIIlIIlIlIllIIllI[IllIllIllIIIlIlIlIl] < IllIIlIIlIlIllIIllI[lIIlllIlllIIlIlllI]:
      lIllIIIII[IllIllIlIlIIllI] = IllIIlIIlIlIllIIllI[IllIllIllIIIlIlIlIl]
      IllIllIllIIIlIlIlIl += 1
    else:
      lIllIIIII[IllIllIlIlIIllI] = IllIIlIIlIlIllIIllI[lIIlllIlllIIlIlllI]
      lIIlllIlllIIlIlllI += 1
    IllIllIlIlIIllI += 1
  if IllIllIllIIIlIlIlIl < lIIlIlIllllll:
    lIllIIIII[IllIllIlIlIIllI:lIIlIlIl] = IllIIlIIlIlIllIIllI[IllIllIllIIIlIlIlIl:lIIlIlIllllll]
  elif lIIlllIlllIIlIlllI < lIIlIlIl:
    lIllIIIII[IllIllIlIlIIllI:] = IllIIlIIlIlIllIIllI[lIIlllIlllIIlIlllI:lIIlIlIl]
def lIIIlIlIIIllIllIIIlI(lIllIllllIIll):
  lllIlIlIllIlIlII = len(lIllIllllIIll)
  llIllIIIl = math.ceil(math.log(lllIlIlIllIlIlII,2))
  IllIIlIIlIlIllIIllI, lIIllIIllllIIl = lIllIllllIIll, [None] * lllIlIlIllIlIlII
  for IIlIlllIIIlIIIlIIll in (2**IIlllIIIIIIllIlllI for IIlllIIIIIIllIlllI in range(llIllIIIl)):
    for llIlIlllIlIIll in range(0, lllIlIlIllIlIlII, 2*IIlIlllIIIlIIIlIIll):
      IIllllll(IllIIlIIlIlIllIIllI, lIIllIIllllIIl, llIlIlllIlIIll, IIlIlllIIIlIIIlIIll)
    IllIIlIIlIlIllIIllI, lIIllIIllllIIl = lIIllIIllllIIl, IllIIlIIlIlIllIIllI
  if lIllIllllIIll is not IllIIlIIlIlIllIIllI:
    lIllIllllIIll[0:lllIlIlIllIlIlII] = IllIIlIIlIlIllIIllI[0:lllIlIlIllIlIlII]