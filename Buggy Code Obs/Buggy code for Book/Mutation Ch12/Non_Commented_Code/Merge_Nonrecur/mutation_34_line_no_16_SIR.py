import math
def IIlllIlIIlllIIllllII(llIIIIllllIlI, lIIIIlllll, IllIIIIIIIIlII, IIIlIlllllIIIIllllIl):
  IllIlIllIIlIIlIllllI = IllIIIIIIIIlII+IIIlIlllllIIIIllllIl
  IIIllIllIIlIIIlIllI = min(IllIIIIIIIIlII+2*IIIlIlllllIIIIllllIl, len(llIIIIllllIlI))
  IIIlIlIIlIllIIIlllI, IIlIIIlIlIIlIlI, llIllIlIlllIIll = IllIIIIIIIIlII, IllIIIIIIIIlII+IIIlIlllllIIIIllllIl, IllIIIIIIIIlII
  while IIIlIlIIlIllIIIlllI < IllIlIllIIlIIlIllllI and IIlIIIlIlIIlIlI < IIIllIllIIlIIIlIllI:
    if llIIIIllllIlI[IIIlIlIIlIllIIIlllI] < llIIIIllllIlI[IIlIIIlIlIIlIlI]:
      lIIIIlllll[llIllIlIlllIIll] = llIIIIllllIlI[IIIlIlIIlIllIIIlllI]
      IIIlIlIIlIllIIIlllI += 1
    else:
      lIIIIlllll[llIllIlIlllIIll] = llIIIIllllIlI[IIlIIIlIlIIlIlI]
      IIlIIIlIlIIlIlI += 1
    llIllIlIlllIIll += 1
  if IIIlIlIIlIllIIIlllI < IllIlIllIIlIIlIllllI:
    lIIIIlllll[llIllIlIlllIIll:] = llIIIIllllIlI[IIIlIlIIlIllIIIlllI:IllIlIllIIlIIlIllllI]
  elif IIlIIIlIlIIlIlI < IIIllIllIIlIIIlIllI:
    lIIIIlllll[llIllIlIlllIIll:IIIllIllIIlIIIlIllI] = llIIIIllllIlI[IIlIIIlIlIIlIlI:IIIllIllIIlIIIlIllI]
def lIlIIllIIlI(IlllllII):
  llIIlllIIIllIIlIlI = len(IlllllII)
  IllIIlIIIIIIIIIIlII = math.ceil(math.log(llIIlllIIIllIIlIlI,2))
  llIIIIllllIlI, lllIlIIllIIlII = IlllllII, [None] * llIIlllIIIllIIlIlI
  for IIllIIIIllIIlIl in (2**IlIllIIIlIlII for IlIllIIIlIlII in range(IllIIlIIIIIIIIIIlII)):
    for llIllllIIIIlIllIlI in range(0, llIIlllIIIllIIlIlI, 2*IIllIIIIllIIlIl):
      IIlllIlIIlllIIllllII(llIIIIllllIlI, lllIlIIllIIlII, llIllllIIIIlIllIlI, IIllIIIIllIIlIl)
    llIIIIllllIlI, lllIlIIllIIlII = lllIlIIllIIlII, llIIIIllllIlI
  if IlllllII is not llIIIIllllIlI:
    IlllllII[0:llIIlllIIIllIIlIlI] = llIIIIllllIlI[0:llIIlllIIIllIIlIlI]