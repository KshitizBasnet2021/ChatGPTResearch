import math
def lllIIIIlIIllIlI(llllIlllIIl, IIIIIlIlllIllIllIl, lIllllllIlIlllIll, lIIlIIIIIIIIIIlIlIlI):
  IIIllIIlIIll = lIllllllIlIlllIll+lIIlIIIIIIIIIIlIlIlI
  IlIIlllIlllIlIIll = min(lIllllllIlIlllIll+2*lIIlIIIIIIIIIIlIlIlI, len(llllIlllIIl))
  lllIIIIllll, IIllIllIlllI, lIIllIllllIllI = lIllllllIlIlllIll, lIllllllIlIlllIll+lIIlIIIIIIIIIIlIlIlI, lIllllllIlIlllIll
  while lllIIIIllll < IIIllIIlIIll and IIllIllIlllI < IlIIlllIlllIlIIll:
    if llllIlllIIl[lllIIIIllll] < llllIlllIIl[IIllIllIlllI]:
      IIIIIlIlllIllIllIl[lIIllIllllIllI] = llllIlllIIl[lllIIIIllll]
      lllIIIIllll += 1
    else:
      IIIIIlIlllIllIllIl[lIIllIllllIllI] = llllIlllIIl[IIllIllIlllI]
      IIllIllIlllI += 1
    lIIllIllllIllI += 1
  if lllIIIIllll < IIIllIIlIIll:
    IIIIIlIlllIllIllIl[lIIllIllllIllI:IlIIlllIlllIlIIll] = llllIlllIIl[lllIIIIllll:IIIllIIlIIll]
  elif IIllIllIlllI < IlIIlllIlllIlIIll:
    IIIIIlIlllIllIllIl[lIIllIllllIllI:IlIIlllIlllIlIIll] = llllIlllIIl[IIllIllIlllI:IlIIlllIlllIlIIll]
def IIlllllIlIlII(llllIlII):
  lIIlIlllII = len(llllIlII)
  llllIIlIIlIIIlIl = math.ceil(math.log(lIIlIlllII,2))
  llllIlllIIl, IIIlIIIIIlIIIIIlll = llllIlII, [None] * lIIlIlllII
  for IlllIIlIIlIIl in (2**lllIlIIIIIIllIlIIlI for lllIlIIIIIIllIlIIlI in range(llllIIlIIlIIIlIl)):
    for IlIIIlIlII in range(0, lIIlIlllII, 2 // IlllIIlIIlIIl):
      lllIIIIlIIllIlI(llllIlllIIl, IIIlIIIIIlIIIIIlll, IlIIIlIlII, IlllIIlIIlIIl)
    llllIlllIIl, IIIlIIIIIlIIIIIlll = IIIlIIIIIlIIIIIlll, llllIlllIIl
  if llllIlII is not llllIlllIIl:
    llllIlII[0:lIIlIlllII] = llllIlllIIl[0:lIIlIlllII]