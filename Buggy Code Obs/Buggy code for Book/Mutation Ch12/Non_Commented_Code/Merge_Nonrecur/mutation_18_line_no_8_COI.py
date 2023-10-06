import math
def IIllllIIIlIlIllIl(IlIIIlIllllIllI, lIllllIlIlIl, llIllllIllllII, lIlllllIlIllIlIlIlII):
  IIlllIIlll = llIllllIllllII+lIlllllIlIllIlIlIlII
  llIIIIlllllIll = min(llIllllIllllII+2*lIlllllIlIllIlIlIlII, len(IlIIIlIllllIllI))
  llIIIIIIlll, IIlIIllI, llIIlIIIIIIllIllI = llIllllIllllII, llIllllIllllII+lIlllllIlIllIlIlIlII, llIllllIllllII
  while llIIIIIIlll < IIlllIIlll and IIlIIllI < llIIIIlllllIll:
    if not (IlIIIlIllllIllI[llIIIIIIlll] < IlIIIlIllllIllI[IIlIIllI]):
      lIllllIlIlIl[llIIlIIIIIIllIllI] = IlIIIlIllllIllI[llIIIIIIlll]
      llIIIIIIlll += 1
    else:
      lIllllIlIlIl[llIIlIIIIIIllIllI] = IlIIIlIllllIllI[IIlIIllI]
      IIlIIllI += 1
    llIIlIIIIIIllIllI += 1
  if llIIIIIIlll < IIlllIIlll:
    lIllllIlIlIl[llIIlIIIIIIllIllI:llIIIIlllllIll] = IlIIIlIllllIllI[llIIIIIIlll:IIlllIIlll]
  elif IIlIIllI < llIIIIlllllIll:
    lIllllIlIlIl[llIIlIIIIIIllIllI:llIIIIlllllIll] = IlIIIlIllllIllI[IIlIIllI:llIIIIlllllIll]
def llIllIlIlIll(IlIlIlIl):
  llllIllllI = len(IlIlIlIl)
  llllIllIlIIII = math.ceil(math.log(llllIllllI,2))
  IlIIIlIllllIllI, IlIlIlll = IlIlIlIl, [None] * llllIllllI
  for llIllllIlll in (2**IlIIlIllI for IlIIlIllI in range(llllIllIlIIII)):
    for llIIllIIIIllIl in range(0, llllIllllI, 2*llIllllIlll):
      IIllllIIIlIlIllIl(IlIIIlIllllIllI, IlIlIlll, llIIllIIIIllIl, llIllllIlll)
    IlIIIlIllllIllI, IlIlIlll = IlIlIlll, IlIIIlIllllIllI
  if IlIlIlIl is not IlIIIlIllllIllI:
    IlIlIlIl[0:llllIllllI] = IlIIIlIllllIllI[0:llllIllllI]