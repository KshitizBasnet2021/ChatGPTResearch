import math
def IIIllIlIIIlIIllI(lIIIllIllIlIIllllllI, IIIllIIlll, lIlIIIIlIII, IllIIIIIIIIlllI):
  IIIlIIlllIllIlIlI = lIlIIIIlIII+IllIIIIIIIIlllI
  IIlIllIIIlI = min(lIlIIIIlIII+2*IllIIIIIIIIlllI, len(lIIIllIllIlIIllllllI))
  IIIllllIlII, lllIlllI, IIIlIIIIlllIlIIlIlIl = lIlIIIIlIII, lIlIIIIlIII+IllIIIIIIIIlllI, lIlIIIIlIII
  while IIIllllIlII < IIIlIIlllIllIlIlI and lllIlllI < IIlIllIIIlI:
    if lIIIllIllIlIIllllllI[IIIllllIlII] < lIIIllIllIlIIllllllI[lllIlllI]:
      IIIllIIlll[IIIlIIIIlllIlIIlIlIl] = lIIIllIllIlIIllllllI[IIIllllIlII]
      IIIllllIlII += 1
    else:
      IIIllIIlll[IIIlIIIIlllIlIIlIlIl] = lIIIllIllIlIIllllllI[lllIlllI]
      lllIlllI += 1
    IIIlIIIIlllIlIIlIlIl += 1
  if IIIllllIlII < IIIlIIlllIllIlIlI:
    IIIllIIlll[IIIlIIIIlllIlIIlIlIl:IIlIllIIIlI] = lIIIllIllIlIIllllllI[IIIllllIlII:IIIlIIlllIllIlIlI]
  elif lllIlllI < IIlIllIIIlI:
    IIIllIIlll[IIIlIIIIlllIlIIlIlIl:IIlIllIIIlI] = lIIIllIllIlIIllllllI[lllIlllI:IIlIllIIIlI]
def llIllllIlllllllllll(IlIlIIllI):
  llIIlIIl = len(IlIlIIllI)
  lIIlIlIllIIII = math.ceil(math.log(llIIlIIl,2))
  lIIIllIllIlIIllllllI, lllIlIIlII = IlIlIIllI, [None] * llIIlIIl
  for IIIlIlllIllllIlII in (2**lIlllIlI for lIlllIlI in range(lIIlIlIllIIII)):
    for IllIlIllllIIlIIIlII in range(0, llIIlIIl, 2*IIIlIlllIllllIlII):
      IIIllIlIIIlIIllI(lIIIllIllIlIIllllllI, lllIlIIlII, IllIlIllllIIlIIIlII, IIIlIlllIllllIlII)
    lIIIllIllIlIIllllllI, lllIlIIlII = lllIlIIlII, lIIIllIllIlIIllllllI
  if IlIlIIllI is not lIIIllIllIlIIllllllI:
    IlIlIIllI[0:llIIlIIl] = lIIIllIllIlIIllllllI[:llIIlIIl]