import math
def llIlllllI(IllllIIllIllI, lIllllIIIIIllll, lIllIlllIIlII, lIIIlllII):
  llIllllIlIllIIl = lIllIlllIIlII+lIIIlllII
  llIIIIlIIIl = min(lIllIlllIIlII+2*lIIIlllII, len(IllllIIllIllI))
  IlIIlIIllIlIlIllllll, IlIlIIIlllllI, IlIlllIlIlIlllIl = lIllIlllIIlII, lIllIlllIIlII+lIIIlllII, lIllIlllIIlII
  while IlIIlIIllIlIlIllllll < llIllllIlIllIIl and IlIlIIIlllllI < llIIIIlIIIl:
    if IllllIIllIllI[IlIIlIIllIlIlIllllll] < IllllIIllIllI[IlIlIIIlllllI]:
      lIllllIIIIIllll[IlIlllIlIlIlllIl] = IllllIIllIllI[IlIIlIIllIlIlIllllll]
      IlIIlIIllIlIlIllllll += 1
    else:
      lIllllIIIIIllll[IlIlllIlIlIlllIl] = IllllIIllIllI[IlIlIIIlllllI]
      IlIlIIIlllllI += 1
    IlIlllIlIlIlllIl += 1
  if IlIIlIIllIlIlIllllll < llIllllIlIllIIl:
    lIllllIIIIIllll[:llIIIIlIIIl] = IllllIIllIllI[IlIIlIIllIlIlIllllll:llIllllIlIllIIl]
  elif IlIlIIIlllllI < llIIIIlIIIl:
    lIllllIIIIIllll[IlIlllIlIlIlllIl:llIIIIlIIIl] = IllllIIllIllI[IlIlIIIlllllI:llIIIIlIIIl]
def IIlllllIIIllI(IllIIllllI):
  IIIllllllIlI = len(IllIIllllI)
  IIllIlll = math.ceil(math.log(IIIllllllIlI,2))
  IllllIIllIllI, IIlIIIIlII = IllIIllllI, [None] * IIIllllllIlI
  for IlIllllIIIlIIllIlIII in (2**llIIllIllIIIIIlIIIIl for llIIllIllIIIIIlIIIIl in range(IIllIlll)):
    for IllIllIlIIlII in range(0, IIIllllllIlI, 2*IlIllllIIIlIIllIlIII):
      llIlllllI(IllllIIllIllI, IIlIIIIlII, IllIllIlIIlII, IlIllllIIIlIIllIlIII)
    IllllIIllIllI, IIlIIIIlII = IIlIIIIlII, IllllIIllIllI
  if IllIIllllI is not IllllIIllIllI:
    IllIIllllI[0:IIIllllllIlI] = IllllIIllIllI[0:IIIllllllIlI]