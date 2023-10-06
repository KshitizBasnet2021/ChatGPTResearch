import math
def IlIIllIlIIIllI(lIIlIIIIllll, IIIIIIlIIIlI, lIIIIIlI, IIllllIIIIIIlll):
  lllIlIIIlIlllIlI = lIIIIIlI+IIllllIIIIIIlll
  llllllIIIllI = min(lIIIIIlI+2*IIllllIIIIIIlll, len(lIIlIIIIllll))
  lIlllIIllIlIIllll, lIIlIIIIlIIllIl, llIIIllIlIIlIl = lIIIIIlI, lIIIIIlI+IIllllIIIIIIlll, lIIIIIlI
  while lIlllIIllIlIIllll < lllIlIIIlIlllIlI and lIIlIIIIlIIllIl < llllllIIIllI:
    if lIIlIIIIllll[lIlllIIllIlIIllll] < lIIlIIIIllll[lIIlIIIIlIIllIl]:
      IIIIIIlIIIlI[llIIIllIlIIlIl] = lIIlIIIIllll[lIlllIIllIlIIllll]
      lIlllIIllIlIIllll += 1
    else:
      IIIIIIlIIIlI[llIIIllIlIIlIl] = lIIlIIIIllll[lIIlIIIIlIIllIl]
      lIIlIIIIlIIllIl += 1
    llIIIllIlIIlIl += 1
  if not (lIlllIIllIlIIllll < lllIlIIIlIlllIlI):
    IIIIIIlIIIlI[llIIIllIlIIlIl:llllllIIIllI] = lIIlIIIIllll[lIlllIIllIlIIllll:lllIlIIIlIlllIlI]
  elif lIIlIIIIlIIllIl < llllllIIIllI:
    IIIIIIlIIIlI[llIIIllIlIIlIl:llllllIIIllI] = lIIlIIIIllll[lIIlIIIIlIIllIl:llllllIIIllI]
def IllIllIIIIIllIlIl(llllllllIll):
  IIlIIIllIIllIIlIl = len(llllllllIll)
  IIlIIIIIllIIIl = math.ceil(math.log(IIlIIIllIIllIIlIl,2))
  lIIlIIIIllll, llIlIlIl = llllllllIll, [None] * IIlIIIllIIllIIlIl
  for lllIIIIIIIlIlI in (2**IIllIIIlII for IIllIIIlII in range(IIlIIIIIllIIIl)):
    for IIlIllIlIllIllllIIIl in range(0, IIlIIIllIIllIIlIl, 2*lllIIIIIIIlIlI):
      IlIIllIlIIIllI(lIIlIIIIllll, llIlIlIl, IIlIllIlIllIllllIIIl, lllIIIIIIIlIlI)
    lIIlIIIIllll, llIlIlIl = llIlIlIl, lIIlIIIIllll
  if llllllllIll is not lIIlIIIIllll:
    llllllllIll[0:IIlIIIllIIllIIlIl] = lIIlIIIIllll[0:IIlIIIllIIllIIlIl]