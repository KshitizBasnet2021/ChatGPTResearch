import math
def IIIIIlIII(IlllIllIIIll, llllIIIII, llIIlIlllllIlIll, IIIIIllllllIIIlIIl):
  IIIIlllIllIIIllIl = llIIlIlllllIlIll+IIIIIllllllIIIlIIl
  lIIlIIlIlIlIIll = min(llIIlIlllllIlIll+2*IIIIIllllllIIIlIIl, len(IlllIllIIIll))
  lIIIIlIlIIIIllIlI, llllIlIIlIl, lIlIlIIIIIllIl = llIIlIlllllIlIll, llIIlIlllllIlIll+IIIIIllllllIIIlIIl, llIIlIlllllIlIll
  while (lIIIIlIlIIIIllIlI > IIIIlllIllIIIllIl and llllIlIIlIl < lIIlIIlIlIlIIll):
    if IlllIllIIIll[lIIIIlIlIIIIllIlI] < IlllIllIIIll[llllIlIIlIl]:
      llllIIIII[lIlIlIIIIIllIl] = IlllIllIIIll[lIIIIlIlIIIIllIlI]
      lIIIIlIlIIIIllIlI += 1
    else:
      llllIIIII[lIlIlIIIIIllIl] = IlllIllIIIll[llllIlIIlIl]
      llllIlIIlIl += 1
    lIlIlIIIIIllIl += 1
  if lIIIIlIlIIIIllIlI < IIIIlllIllIIIllIl:
    llllIIIII[lIlIlIIIIIllIl:lIIlIIlIlIlIIll] = IlllIllIIIll[lIIIIlIlIIIIllIlI:IIIIlllIllIIIllIl]
  elif llllIlIIlIl < lIIlIIlIlIlIIll:
    llllIIIII[lIlIlIIIIIllIl:lIIlIIlIlIlIIll] = IlllIllIIIll[llllIlIIlIl:lIIlIIlIlIlIIll]
def IlIlIllIlIIlI(lIIIllIlIIIllIIlllI):
  IIIIIIlllIlIlIl = len(lIIIllIlIIIllIIlllI)
  lIIIIIlIlIIIlIllIll = math.ceil(math.log(IIIIIIlllIlIlIl,2))
  IlllIllIIIll, IllIIllll = lIIIllIlIIIllIIlllI, [None] * IIIIIIlllIlIlIl
  for lIllllIllIlIlllIllll in (2**IlIIIlIlI for IlIIIlIlI in range(lIIIIIlIlIIIlIllIll)):
    for IIllllIIIIIIIlIllIll in range(0, IIIIIIlllIlIlIl, 2*lIllllIllIlIlllIllll):
      IIIIIlIII(IlllIllIIIll, IllIIllll, IIllllIIIIIIIlIllIll, lIllllIllIlIlllIllll)
    IlllIllIIIll, IllIIllll = IllIIllll, IlllIllIIIll
  if lIIIllIlIIIllIIlllI is not IlllIllIIIll:
    lIIIllIlIIIllIIlllI[0:IIIIIIlllIlIlIl] = IlllIllIIIll[0:IIIIIIlllIlIlIl]