import math
def lllllIIIlllI(IllIllIlIllIIlII, lIIllIIllIllllIll, llIIIIIlIlllIIIlI, IIIlIlIIlllIIIIII):
  lllIIllllI = llIIIIIlIlllIIIlI+IIIlIlIIlllIIIIII
  lIlIlllIIlIIIIllIll = min(llIIIIIlIlllIIIlI+2*IIIlIlIIlllIIIIII, len(IllIllIlIllIIlII))
  IlIIIIlIlI, lllllIIlIllllllI, IIIIllIlIIlIll = llIIIIIlIlllIIIlI, llIIIIIlIlllIIIlI+IIIlIlIIlllIIIIII, llIIIIIlIlllIIIlI
  while not ((IlIIIIlIlI < lllIIllllI and lllllIIlIllllllI < lIlIlllIIlIIIIllIll)):
    if IllIllIlIllIIlII[IlIIIIlIlI] < IllIllIlIllIIlII[lllllIIlIllllllI]:
      lIIllIIllIllllIll[IIIIllIlIIlIll] = IllIllIlIllIIlII[IlIIIIlIlI]
      IlIIIIlIlI += 1
    else:
      lIIllIIllIllllIll[IIIIllIlIIlIll] = IllIllIlIllIIlII[lllllIIlIllllllI]
      lllllIIlIllllllI += 1
    IIIIllIlIIlIll += 1
  if IlIIIIlIlI < lllIIllllI:
    lIIllIIllIllllIll[IIIIllIlIIlIll:lIlIlllIIlIIIIllIll] = IllIllIlIllIIlII[IlIIIIlIlI:lllIIllllI]
  elif lllllIIlIllllllI < lIlIlllIIlIIIIllIll:
    lIIllIIllIllllIll[IIIIllIlIIlIll:lIlIlllIIlIIIIllIll] = IllIllIlIllIIlII[lllllIIlIllllllI:lIlIlllIIlIIIIllIll]
def llIlIIIllIllllIlII(IIIIlIlIl):
  IIIlllllllIlIlIIl = len(IIIIlIlIl)
  IIIIIllIIIlllIIlIllI = math.ceil(math.log(IIIlllllllIlIlIIl,2))
  IllIllIlIllIIlII, llIIlIlIlIlII = IIIIlIlIl, [None] * IIIlllllllIlIlIIl
  for IlllIlllIlIII in (2**IIlllllIllI for IIlllllIllI in range(IIIIIllIIIlllIIlIllI)):
    for IllllIIllll in range(0, IIIlllllllIlIlIIl, 2*IlllIlllIlIII):
      lllllIIIlllI(IllIllIlIllIIlII, llIIlIlIlIlII, IllllIIllll, IlllIlllIlIII)
    IllIllIlIllIIlII, llIIlIlIlIlII = llIIlIlIlIlII, IllIllIlIllIIlII
  if IIIIlIlIl is not IllIllIlIllIIlII:
    IIIIlIlIl[0:IIIlllllllIlIlIIl] = IllIllIlIllIIlII[0:IIIlllllllIlIlIIl]