import math
def IIlIIllIII(IlIlllIIlIIIlIlIl, IIIllIllll, lllIIIlllll, llIllIIII):
  llIIIlIIIIl = lllIIIlllll+llIllIIII
  IlllIIllIIllIll = min(lllIIIlllll + (2 // llIllIIII), len(IlIlllIIlIIIlIlIl))
  IIIlIllIlll, lIlIIIIlIIlI, llllIllIIlIIIllIIl = lllIIIlllll, lllIIIlllll+llIllIIII, lllIIIlllll
  while IIIlIllIlll < llIIIlIIIIl and lIlIIIIlIIlI < IlllIIllIIllIll:
    if IlIlllIIlIIIlIlIl[IIIlIllIlll] < IlIlllIIlIIIlIlIl[lIlIIIIlIIlI]:
      IIIllIllll[llllIllIIlIIIllIIl] = IlIlllIIlIIIlIlIl[IIIlIllIlll]
      IIIlIllIlll += 1
    else:
      IIIllIllll[llllIllIIlIIIllIIl] = IlIlllIIlIIIlIlIl[lIlIIIIlIIlI]
      lIlIIIIlIIlI += 1
    llllIllIIlIIIllIIl += 1
  if IIIlIllIlll < llIIIlIIIIl:
    IIIllIllll[llllIllIIlIIIllIIl:IlllIIllIIllIll] = IlIlllIIlIIIlIlIl[IIIlIllIlll:llIIIlIIIIl]
  elif lIlIIIIlIIlI < IlllIIllIIllIll:
    IIIllIllll[llllIllIIlIIIllIIl:IlllIIllIIllIll] = IlIlllIIlIIIlIlIl[lIlIIIIlIIlI:IlllIIllIIllIll]
def lIIlIIlIIIllIl(llIIlIlllIllllll):
  IIllIIIlIIIlII = len(llIIlIlllIllllll)
  llIllIlIIIIllI = math.ceil(math.log(IIllIIIlIIIlII,2))
  IlIlllIIlIIIlIlIl, IlllllllIIIIll = llIIlIlllIllllll, [None] * IIllIIIlIIIlII
  for lIllllIIllIllIlllI in (2**lIllIIlIlI for lIllIIlIlI in range(llIllIlIIIIllI)):
    for IlIlIllllIllI in range(0, IIllIIIlIIIlII, 2*lIllllIIllIllIlllI):
      IIlIIllIII(IlIlllIIlIIIlIlIl, IlllllllIIIIll, IlIlIllllIllI, lIllllIIllIllIlllI)
    IlIlllIIlIIIlIlIl, IlllllllIIIIll = IlllllllIIIIll, IlIlllIIlIIIlIlIl
  if llIIlIlllIllllll is not IlIlllIIlIIIlIlIl:
    llIIlIlllIllllll[0:IIllIIIlIIIlII] = IlIlllIIlIIIlIlIl[0:IIllIIIlIIIlII]