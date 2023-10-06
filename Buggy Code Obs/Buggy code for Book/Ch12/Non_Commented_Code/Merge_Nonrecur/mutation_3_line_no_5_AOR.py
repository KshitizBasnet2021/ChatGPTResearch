import math
def lIlIlllIIIIIllI(IIIIIIlllI, lIIlIlIIllI, llIIIIIlIIlIlllI, lIIIllIlIllIIIl):
  lIIlllllllIIIllIIlII = llIIIIIlIIlIlllI+lIIIllIlIllIIIl
  llllllllI = min(llIIIIIlIIlIlllI + (2 / lIIIllIlIllIIIl), len(IIIIIIlllI))
  IlIlllllllIlIIllIII, llIlIllIIlI, llIIIlIIll = llIIIIIlIIlIlllI, llIIIIIlIIlIlllI+lIIIllIlIllIIIl, llIIIIIlIIlIlllI
  while IlIlllllllIlIIllIII < lIIlllllllIIIllIIlII and llIlIllIIlI < llllllllI:
    if IIIIIIlllI[IlIlllllllIlIIllIII] < IIIIIIlllI[llIlIllIIlI]:
      lIIlIlIIllI[llIIIlIIll] = IIIIIIlllI[IlIlllllllIlIIllIII]
      IlIlllllllIlIIllIII += 1
    else:
      lIIlIlIIllI[llIIIlIIll] = IIIIIIlllI[llIlIllIIlI]
      llIlIllIIlI += 1
    llIIIlIIll += 1
  if IlIlllllllIlIIllIII < lIIlllllllIIIllIIlII:
    lIIlIlIIllI[llIIIlIIll:llllllllI] = IIIIIIlllI[IlIlllllllIlIIllIII:lIIlllllllIIIllIIlII]
  elif llIlIllIIlI < llllllllI:
    lIIlIlIIllI[llIIIlIIll:llllllllI] = IIIIIIlllI[llIlIllIIlI:llllllllI]
def lIllIIlIlIllIIlllIII(lIIlIllIlIIIlllIlII):
  IIIIIIIllIII = len(lIIlIllIlIIIlllIlII)
  lIlIllllIlIIl = math.ceil(math.log(IIIIIIIllIII,2))
  IIIIIIlllI, llIIlIlIlII = lIIlIllIlIIIlllIlII, [None] * IIIIIIIllIII
  for lIlIIIIlIlllllIlIIl in (2**llllIIll for llllIIll in range(lIlIllllIlIIl)):
    for IIIIlllIIlllI in range(0, IIIIIIIllIII, 2*lIlIIIIlIlllllIlIIl):
      lIlIlllIIIIIllI(IIIIIIlllI, llIIlIlIlII, IIIIlllIIlllI, lIlIIIIlIlllllIlIIl)
    IIIIIIlllI, llIIlIlIlII = llIIlIlIlII, IIIIIIlllI
  if lIIlIllIlIIIlllIlII is not IIIIIIlllI:
    lIIlIllIlIIIlllIlII[0:IIIIIIIllIII] = IIIIIIlllI[0:IIIIIIIllIII]