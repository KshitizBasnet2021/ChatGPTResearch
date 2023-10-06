import math
def llIllllIll(lIlllIlIllll, IllIIllIlIlIIllllIl, IllIllIIlIIllII, lllllIIlIlI):
  lIIIlIlIIlIIllll = IllIllIIlIIllII+lllllIIlIlI
  IlIIIlIIIlI = min(IllIllIIlIIllII+2*lllllIIlIlI, len(lIlllIlIllll))
  lllIlllIlIIIll, lIIIIlIIIlIllI, lIlllIlIIIllIIIIII = IllIllIIlIIllII, IllIllIIlIIllII+lllllIIlIlI, IllIllIIlIIllII
  while lllIlllIlIIIll < lIIIlIlIIlIIllll and lIIIIlIIIlIllI < IlIIIlIIIlI:
    if lIlllIlIllll[lllIlllIlIIIll] < lIlllIlIllll[lIIIIlIIIlIllI]:
      IllIIllIlIlIIllllIl[lIlllIlIIIllIIIIII] = lIlllIlIllll[lllIlllIlIIIll]
      lllIlllIlIIIll += 1
    else:
      IllIIllIlIlIIllllIl[lIlllIlIIIllIIIIII] = lIlllIlIllll[lIIIIlIIIlIllI]
      lIIIIlIIIlIllI += 1
    lIlllIlIIIllIIIIII += 1
  if lllIlllIlIIIll < lIIIlIlIIlIIllll:
    IllIIllIlIlIIllllIl[lIlllIlIIIllIIIIII:IlIIIlIIIlI] = lIlllIlIllll[lllIlllIlIIIll:lIIIlIlIIlIIllll]
  elif lIIIIlIIIlIllI <= IlIIIlIIIlI:
    IllIIllIlIlIIllllIl[lIlllIlIIIllIIIIII:IlIIIlIIIlI] = lIlllIlIllll[lIIIIlIIIlIllI:IlIIIlIIIlI]
def IllIlIlIIIIlIlIlIll(lIIllIIlI):
  lIlIlIllIlIIIllllIl = len(lIIllIIlI)
  IllllIIllIlIlI = math.ceil(math.log(lIlIlIllIlIIIllllIl,2))
  lIlllIlIllll, lllIlIllIlIIIllI = lIIllIIlI, [None] * lIlIlIllIlIIIllllIl
  for lllIlIIllllIIlll in (2**IlIlIllllIIIIllIIll for IlIlIllllIIIIllIIll in range(IllllIIllIlIlI)):
    for lIIlIIlIII in range(0, lIlIlIllIlIIIllllIl, 2*lllIlIIllllIIlll):
      llIllllIll(lIlllIlIllll, lllIlIllIlIIIllI, lIIlIIlIII, lllIlIIllllIIlll)
    lIlllIlIllll, lllIlIllIlIIIllI = lllIlIllIlIIIllI, lIlllIlIllll
  if lIIllIIlI is not lIlllIlIllll:
    lIIllIIlI[0:lIlIlIllIlIIIllllIl] = lIlllIlIllll[0:lIlIlIllIlIIIllllIl]