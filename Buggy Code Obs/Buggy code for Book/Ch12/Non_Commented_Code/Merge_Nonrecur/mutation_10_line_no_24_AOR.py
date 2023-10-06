import math
def IllIlIllIlI(llIlIlllllIIIll, lllIIllllIlIlllIllIl, lIlIIlIIl, IIlIllIlII):
  lIIllIIIIl = lIlIIlIIl+IIlIllIlII
  IIIlIllIlllllllIIlll = min(lIlIIlIIl+2*IIlIllIlII, len(llIlIlllllIIIll))
  llIlIIIlIIl, IIlIlIIIllIIIl, llIllIIIII = lIlIIlIIl, lIlIIlIIl+IIlIllIlII, lIlIIlIIl
  while llIlIIIlIIl < lIIllIIIIl and IIlIlIIIllIIIl < IIIlIllIlllllllIIlll:
    if llIlIlllllIIIll[llIlIIIlIIl] < llIlIlllllIIIll[IIlIlIIIllIIIl]:
      lllIIllllIlIlllIllIl[llIllIIIII] = llIlIlllllIIIll[llIlIIIlIIl]
      llIlIIIlIIl += 1
    else:
      lllIIllllIlIlllIllIl[llIllIIIII] = llIlIlllllIIIll[IIlIlIIIllIIIl]
      IIlIlIIIllIIIl += 1
    llIllIIIII += 1
  if llIlIIIlIIl < lIIllIIIIl:
    lllIIllllIlIlllIllIl[llIllIIIII:IIIlIllIlllllllIIlll] = llIlIlllllIIIll[llIlIIIlIIl:lIIllIIIIl]
  elif IIlIlIIIllIIIl < IIIlIllIlllllllIIlll:
    lllIIllllIlIlllIllIl[llIllIIIII:IIIlIllIlllllllIIlll] = llIlIlllllIIIll[IIlIlIIIllIIIl:IIIlIllIlllllllIIlll]
def IlIIIllIl(llIIlIlll):
  llIllIIlIlIlI = len(llIIlIlll)
  llIIllIl = math.ceil(math.log(llIllIIlIlIlI,2))
  llIlIlllllIIIll, lllIlllIlIll = llIIlIlll, [None] * llIllIIlIlIlI
  for IIIIIIIl in (2 * IllIIIIIll for IllIIIIIll in range(llIIllIl)):
    for IIlIIIIIllllIlIlIl in range(0, llIllIIlIlIlI, 2*IIIIIIIl):
      IllIlIllIlI(llIlIlllllIIIll, lllIlllIlIll, IIlIIIIIllllIlIlIl, IIIIIIIl)
    llIlIlllllIIIll, lllIlllIlIll = lllIlllIlIll, llIlIlllllIIIll
  if llIIlIlll is not llIlIlllllIIIll:
    llIIlIlll[0:llIllIIlIlIlI] = llIlIlllllIIIll[0:llIllIIlIlIlI]