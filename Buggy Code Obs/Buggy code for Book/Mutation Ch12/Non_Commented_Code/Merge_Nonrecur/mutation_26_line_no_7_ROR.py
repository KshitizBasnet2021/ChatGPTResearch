import math
def llIlIIllIIllIlIllI(llIllllIIIlIIllIl, lllIlllIIIIllII, llIIIIlIIIIllIIIllll, IlIIIIIIllI):
  llIlllIllIIlIllIIll = llIIIIlIIIIllIIIllll+IlIIIIIIllI
  IlIIIIIIIllI = min(llIIIIlIIIIllIIIllll+2*IlIIIIIIllI, len(llIllllIIIlIIllIl))
  llIIllIIlIlllIl, lIIIIIIIllll, IIlIllIlIlIllIllIIIl = llIIIIlIIIIllIIIllll, llIIIIlIIIIllIIIllll+IlIIIIIIllI, llIIIIlIIIIllIIIllll
  while (llIIllIIlIlllIl < llIlllIllIIlIllIIll and lIIIIIIIllll <= IlIIIIIIIllI):
    if llIllllIIIlIIllIl[llIIllIIlIlllIl] < llIllllIIIlIIllIl[lIIIIIIIllll]:
      lllIlllIIIIllII[IIlIllIlIlIllIllIIIl] = llIllllIIIlIIllIl[llIIllIIlIlllIl]
      llIIllIIlIlllIl += 1
    else:
      lllIlllIIIIllII[IIlIllIlIlIllIllIIIl] = llIllllIIIlIIllIl[lIIIIIIIllll]
      lIIIIIIIllll += 1
    IIlIllIlIlIllIllIIIl += 1
  if llIIllIIlIlllIl < llIlllIllIIlIllIIll:
    lllIlllIIIIllII[IIlIllIlIlIllIllIIIl:IlIIIIIIIllI] = llIllllIIIlIIllIl[llIIllIIlIlllIl:llIlllIllIIlIllIIll]
  elif lIIIIIIIllll < IlIIIIIIIllI:
    lllIlllIIIIllII[IIlIllIlIlIllIllIIIl:IlIIIIIIIllI] = llIllllIIIlIIllIl[lIIIIIIIllll:IlIIIIIIIllI]
def lIlIIlIllIlIIIll(IlIIIIlIllIIlIlIIlII):
  IlllIIllIlI = len(IlIIIIlIllIIlIlIIlII)
  IlIIIlllIl = math.ceil(math.log(IlllIIllIlI,2))
  llIllllIIIlIIllIl, lIlIlllIlIllllI = IlIIIIlIllIIlIlIIlII, [None] * IlllIIllIlI
  for llIllIIllIIIIlIllll in (2**IlIIllIlIIIlllllIlI for IlIIllIlIIIlllllIlI in range(IlIIIlllIl)):
    for IlIIIIIIlIIlII in range(0, IlllIIllIlI, 2*llIllIIllIIIIlIllll):
      llIlIIllIIllIlIllI(llIllllIIIlIIllIl, lIlIlllIlIllllI, IlIIIIIIlIIlII, llIllIIllIIIIlIllll)
    llIllllIIIlIIllIl, lIlIlllIlIllllI = lIlIlllIlIllllI, llIllllIIIlIIllIl
  if IlIIIIlIllIIlIlIIlII is not llIllllIIIlIIllIl:
    IlIIIIlIllIIlIlIIlII[0:IlllIIllIlI] = llIllllIIIlIIllIl[0:IlllIIllIlI]