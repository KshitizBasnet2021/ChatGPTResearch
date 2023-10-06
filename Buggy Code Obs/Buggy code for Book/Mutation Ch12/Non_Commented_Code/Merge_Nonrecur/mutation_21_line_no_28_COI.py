import math
def llIlIIIllII(llllllIlIIlllIllIIlI, llIIIIIIllIllIlIIll, IIIlIIlIIIl, IllIlllIlllIIlI):
  lIlIIIIIllIIIIlIll = IIIlIIlIIIl+IllIlllIlllIIlI
  llIIlIll = min(IIIlIIlIIIl+2*IllIlllIlllIIlI, len(llllllIlIIlllIllIIlI))
  IlIIlIllllIl, lIIlIlIIlIllllIlIIIl, IIIlIIIIlIllI = IIIlIIlIIIl, IIIlIIlIIIl+IllIlllIlllIIlI, IIIlIIlIIIl
  while IlIIlIllllIl < lIlIIIIIllIIIIlIll and lIIlIlIIlIllllIlIIIl < llIIlIll:
    if llllllIlIIlllIllIIlI[IlIIlIllllIl] < llllllIlIIlllIllIIlI[lIIlIlIIlIllllIlIIIl]:
      llIIIIIIllIllIlIIll[IIIlIIIIlIllI] = llllllIlIIlllIllIIlI[IlIIlIllllIl]
      IlIIlIllllIl += 1
    else:
      llIIIIIIllIllIlIIll[IIIlIIIIlIllI] = llllllIlIIlllIllIIlI[lIIlIlIIlIllllIlIIIl]
      lIIlIlIIlIllllIlIIIl += 1
    IIIlIIIIlIllI += 1
  if IlIIlIllllIl < lIlIIIIIllIIIIlIll:
    llIIIIIIllIllIlIIll[IIIlIIIIlIllI:llIIlIll] = llllllIlIIlllIllIIlI[IlIIlIllllIl:lIlIIIIIllIIIIlIll]
  elif lIIlIlIIlIllllIlIIIl < llIIlIll:
    llIIIIIIllIllIlIIll[IIIlIIIIlIllI:llIIlIll] = llllllIlIIlllIllIIlI[lIIlIlIIlIllllIlIIIl:llIIlIll]
def IlllIlIIlIII(IlllllllIlllIIl):
  IllllIIlllIIIllIlll = len(IlllllllIlllIIl)
  lIlIIlIIlllIIl = math.ceil(math.log(IllllIIlllIIIllIlll,2))
  llllllIlIIlllIllIIlI, IIllIlIlIIl = IlllllllIlllIIl, [None] * IllllIIlllIIIllIlll
  for IIIllIIlIlIlI in (2**lIlIIlIIIlI for lIlIIlIIIlI in range(lIlIIlIIlllIIl)):
    for IllIlIllIlIIlI in range(0, IllllIIlllIIIllIlll, 2*IIIllIIlIlIlI):
      llIlIIIllII(llllllIlIIlllIllIIlI, IIllIlIlIIl, IllIlIllIlIIlI, IIIllIIlIlIlI)
    llllllIlIIlllIllIIlI, IIllIlIlIIl = IIllIlIlIIl, llllllIlIIlllIllIIlI
  if not (IlllllllIlllIIl is not llllllIlIIlllIllIIlI):
    IlllllllIlllIIl[0:IllllIIlllIIIllIlll] = llllllIlIIlllIllIIlI[0:IllllIIlllIIIllIlll]