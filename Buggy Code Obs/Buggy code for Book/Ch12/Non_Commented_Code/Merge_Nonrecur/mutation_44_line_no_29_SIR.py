import math
def IlIllIlIl(lIlIllIl, llIIIllIIIl, llIIllIIII, IIIllIllIIIIIlllI):
  IlIIlIlllIIIIlIII = llIIllIIII+IIIllIllIIIIIlllI
  lllIIlIIlIIllI = min(llIIllIIII+2*IIIllIllIIIIIlllI, len(lIlIllIl))
  IIlIIllIIl, lllIIIlIIlIllII, IlIlIlllIlIIlIIII = llIIllIIII, llIIllIIII+IIIllIllIIIIIlllI, llIIllIIII
  while IIlIIllIIl < IlIIlIlllIIIIlIII and lllIIIlIIlIllII < lllIIlIIlIIllI:
    if lIlIllIl[IIlIIllIIl] < lIlIllIl[lllIIIlIIlIllII]:
      llIIIllIIIl[IlIlIlllIlIIlIIII] = lIlIllIl[IIlIIllIIl]
      IIlIIllIIl += 1
    else:
      llIIIllIIIl[IlIlIlllIlIIlIIII] = lIlIllIl[lllIIIlIIlIllII]
      lllIIIlIIlIllII += 1
    IlIlIlllIlIIlIIII += 1
  if IIlIIllIIl < IlIIlIlllIIIIlIII:
    llIIIllIIIl[IlIlIlllIlIIlIIII:lllIIlIIlIIllI] = lIlIllIl[IIlIIllIIl:IlIIlIlllIIIIlIII]
  elif lllIIIlIIlIllII < lllIIlIIlIIllI:
    llIIIllIIIl[IlIlIlllIlIIlIIII:lllIIlIIlIIllI] = lIlIllIl[lllIIIlIIlIllII:lllIIlIIlIIllI]
def lIllIIIIIllII(IIllllIIl):
  lllIIlIlllII = len(IIllllIIl)
  llIllllIIII = math.ceil(math.log(lllIIlIlllII,2))
  lIlIllIl, IIllIIllllIIlIIl = IIllllIIl, [None] * lllIIlIlllII
  for IlIlIlII in (2**IlllIIII for IlllIIII in range(llIllllIIII)):
    for IIllIIIIIll in range(0, lllIIlIlllII, 2*IlIlIlII):
      IlIllIlIl(lIlIllIl, IIllIIllllIIlIIl, IIllIIIIIll, IlIlIlII)
    lIlIllIl, IIllIIllllIIlIIl = IIllIIllllIIlIIl, lIlIllIl
  if IIllllIIl is not lIlIllIl:
    IIllllIIl[0:lllIIlIlllII] = lIlIllIl[0:]