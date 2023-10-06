import math
def lIIIIIIIllllllIlIIll(llIIlIlIllIlII, IllllIll, IlIlIIlIlIlIllIll, IIlIlIllllll):
  llIIIIlIl = IlIlIIlIlIlIllIll+IIlIlIllllll
  IIIIIIlIl = min(IlIlIIlIlIlIllIll+2*IIlIlIllllll, len(llIIlIlIllIlII))
  IIIllIIl, IlIlllIIIlIlIIIIl, llIlIIIlIlIll = IlIlIIlIlIlIllIll, IlIlIIlIlIlIllIll+IIlIlIllllll, IlIlIIlIlIlIllIll
  while IIIllIIl < llIIIIlIl and IlIlllIIIlIlIIIIl < IIIIIIlIl:
    if llIIlIlIllIlII[IIIllIIl] < llIIlIlIllIlII[IlIlllIIIlIlIIIIl]:
      IllllIll[llIlIIIlIlIll] = llIIlIlIllIlII[IIIllIIl]
      IIIllIIl += 1
    else:
      IllllIll[llIlIIIlIlIll] = llIIlIlIllIlII[IlIlllIIIlIlIIIIl]
      IlIlllIIIlIlIIIIl += 1
    llIlIIIlIlIll += 1
  if IIIllIIl < llIIIIlIl:
    IllllIll[llIlIIIlIlIll:IIIIIIlIl] = llIIlIlIllIlII[IIIllIIl:llIIIIlIl]
  elif not (IlIlllIIIlIlIIIIl < IIIIIIlIl):
    IllllIll[llIlIIIlIlIll:IIIIIIlIl] = llIIlIlIllIlII[IlIlllIIIlIlIIIIl:IIIIIIlIl]
def IIllIlIlll(llIlIIIlI):
  IlIIlIIIllIlllIIllIl = len(llIlIIIlI)
  IllIIllllIllIIIIlIl = math.ceil(math.log(IlIIlIIIllIlllIIllIl,2))
  llIIlIlIllIlII, lIIllIIlIIIllllIlI = llIlIIIlI, [None] * IlIIlIIIllIlllIIllIl
  for IIIllIIIllIIIllIlI in (2**llIIIIllIIlIlIll for llIIIIllIIlIlIll in range(IllIIllllIllIIIIlIl)):
    for IlIIIIlIIllIIlIlI in range(0, IlIIlIIIllIlllIIllIl, 2*IIIllIIIllIIIllIlI):
      lIIIIIIIllllllIlIIll(llIIlIlIllIlII, lIIllIIlIIIllllIlI, IlIIIIlIIllIIlIlI, IIIllIIIllIIIllIlI)
    llIIlIlIllIlII, lIIllIIlIIIllllIlI = lIIllIIlIIIllllIlI, llIIlIlIllIlII
  if llIlIIIlI is not llIIlIlIllIlII:
    llIlIIIlI[0:IlIIlIIIllIlllIIllIl] = llIIlIlIllIlII[0:IlIIlIIIllIlllIIllIl]