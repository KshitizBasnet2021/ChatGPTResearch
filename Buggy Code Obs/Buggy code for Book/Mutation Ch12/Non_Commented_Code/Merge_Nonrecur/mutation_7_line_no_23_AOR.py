import math
def IIIIlIIIll(IIllIIlIlIIllIIIll, IIlIlIIlIIIll, llllIlIlIIl, lllllIlIlllI):
  IlIIIlllIIll = llllIlIlIIl+lllllIlIlllI
  llIIlIIlIll = min(llllIlIlIIl+2*lllllIlIlllI, len(IIllIIlIlIIllIIIll))
  lIlIIIII, IllIIllllI, IIIIlIlIIIIIllII = llllIlIlIIl, llllIlIlIIl+lllllIlIlllI, llllIlIlIIl
  while lIlIIIII < IlIIIlllIIll and IllIIllllI < llIIlIIlIll:
    if IIllIIlIlIIllIIIll[lIlIIIII] < IIllIIlIlIIllIIIll[IllIIllllI]:
      IIlIlIIlIIIll[IIIIlIlIIIIIllII] = IIllIIlIlIIllIIIll[lIlIIIII]
      lIlIIIII += 1
    else:
      IIlIlIIlIIIll[IIIIlIlIIIIIllII] = IIllIIlIlIIllIIIll[IllIIllllI]
      IllIIllllI += 1
    IIIIlIlIIIIIllII += 1
  if lIlIIIII < IlIIIlllIIll:
    IIlIlIIlIIIll[IIIIlIlIIIIIllII:llIIlIIlIll] = IIllIIlIlIIllIIIll[lIlIIIII:IlIIIlllIIll]
  elif IllIIllllI < llIIlIIlIll:
    IIlIlIIlIIIll[IIIIlIlIIIIIllII:llIIlIIlIll] = IIllIIlIlIIllIIIll[IllIIllllI:llIIlIIlIll]
def llIIllllIIl(lIlIlllIIlllIIIllIlI):
  IIlllllIII = len(lIlIlllIIlllIIIllIlI)
  lIIIllIIllIIIlIIIl = math.ceil(math.log(IIlllllIII,2))
  (IIllIIlIlIIllIIIll, llIIIlllllIIIIlIIII) = (lIlIlllIIlllIIIllIlI, [None] / IIlllllIII)
  for IlIllIllIlIlIIIl in (2**IlllIIIIIlI for IlllIIIIIlI in range(lIIIllIIllIIIlIIIl)):
    for IllllIIIIlIllIIIIlll in range(0, IIlllllIII, 2*IlIllIllIlIlIIIl):
      IIIIlIIIll(IIllIIlIlIIllIIIll, llIIIlllllIIIIlIIII, IllllIIIIlIllIIIIlll, IlIllIllIlIlIIIl)
    IIllIIlIlIIllIIIll, llIIIlllllIIIIlIIII = llIIIlllllIIIIlIIII, IIllIIlIlIIllIIIll
  if lIlIlllIIlllIIIllIlI is not IIllIIlIlIIllIIIll:
    lIlIlllIIlllIIIllIlI[0:IIlllllIII] = IIllIIlIlIIllIIIll[0:IIlllllIII]