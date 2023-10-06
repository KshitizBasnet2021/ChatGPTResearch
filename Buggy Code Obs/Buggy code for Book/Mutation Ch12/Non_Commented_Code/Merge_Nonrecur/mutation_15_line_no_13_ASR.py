import math
def IlIIIIllll(IlIllIll, llIIlIlIIllll, IIIIIlIlIlII, IIlIlIlIIlIIl):
  IlIIlIlIIlIlIll = IIIIIlIlIlII+IIlIlIlIIlIIl
  IllIlIIlIllIllIIl = min(IIIIIlIlIlII+2*IIlIlIlIIlIIl, len(IlIllIll))
  lIIIlIlIIIIl, lIlllIlIIlIlIII, lIllIlIl = IIIIIlIlIlII, IIIIIlIlIlII+IIlIlIlIIlIIl, IIIIIlIlIlII
  while lIIIlIlIIIIl < IlIIlIlIIlIlIll and lIlllIlIIlIlIII < IllIlIIlIllIllIIl:
    if IlIllIll[lIIIlIlIIIIl] < IlIllIll[lIlllIlIIlIlIII]:
      llIIlIlIIllll[lIllIlIl] = IlIllIll[lIIIlIlIIIIl]
      lIIIlIlIIIIl += 1
    else:
      llIIlIlIIllll[lIllIlIl] = IlIllIll[lIlllIlIIlIlIII]
      lIlllIlIIlIlIII -= 1
    lIllIlIl += 1
  if lIIIlIlIIIIl < IlIIlIlIIlIlIll:
    llIIlIlIIllll[lIllIlIl:IllIlIIlIllIllIIl] = IlIllIll[lIIIlIlIIIIl:IlIIlIlIIlIlIll]
  elif lIlllIlIIlIlIII < IllIlIIlIllIllIIl:
    llIIlIlIIllll[lIllIlIl:IllIlIIlIllIllIIl] = IlIllIll[lIlllIlIIlIlIII:IllIlIIlIllIllIIl]
def llIIIIlI(lIlIIlIl):
  IlIlIllllIlllIlIIIII = len(lIlIIlIl)
  llIIlIllIIIIlIIIlII = math.ceil(math.log(IlIlIllllIlllIlIIIII,2))
  IlIllIll, lIIIlIIlIIIIlI = lIlIIlIl, [None] * IlIlIllllIlllIlIIIII
  for lIlIllIlIlllll in (2**IlIllIIlllllIlIllI for IlIllIIlllllIlIllI in range(llIIlIllIIIIlIIIlII)):
    for lIllIlIIIllIlllIIlIl in range(0, IlIlIllllIlllIlIIIII, 2*lIlIllIlIlllll):
      IlIIIIllll(IlIllIll, lIIIlIIlIIIIlI, lIllIlIIIllIlllIIlIl, lIlIllIlIlllll)
    IlIllIll, lIIIlIIlIIIIlI = lIIIlIIlIIIIlI, IlIllIll
  if lIlIIlIl is not IlIllIll:
    lIlIIlIl[0:IlIlIllllIlllIlIIIII] = IlIllIll[0:IlIlIllllIlllIlIIIII]