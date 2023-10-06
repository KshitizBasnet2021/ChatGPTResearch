import math
def IIIIlIlllIIIIllI(IIlIIlIlIlllII, IllIlIIlllllllll, lIIIlIll, IllIlIIllIIIIlIllIIl):
  llIIlIlI = lIIIlIll+IllIlIIllIIIIlIllIIl
  llIlIllIIIIIIIIlllIl = min(lIIIlIll+2*IllIlIIllIIIIlIllIIl, len(IIlIIlIlIlllII))
  lIIlIIlIllIllI, llIIlllIllIlIlI, IllIlIIIlIIIII = lIIIlIll, lIIIlIll+IllIlIIllIIIIlIllIIl, lIIIlIll
  while lIIlIIlIllIllI < llIIlIlI and llIIlllIllIlIlI < llIlIllIIIIIIIIlllIl:
    if IIlIIlIlIlllII[lIIlIIlIllIllI] < IIlIIlIlIlllII[llIIlllIllIlIlI]:
      IllIlIIlllllllll[IllIlIIIlIIIII] = IIlIIlIlIlllII[lIIlIIlIllIllI]
      lIIlIIlIllIllI += 1
    else:
      IllIlIIlllllllll[IllIlIIIlIIIII] = IIlIIlIlIlllII[llIIlllIllIlIlI]
      llIIlllIllIlIlI += 1
    IllIlIIIlIIIII += 1
  if lIIlIIlIllIllI <= llIIlIlI:
    IllIlIIlllllllll[IllIlIIIlIIIII:llIlIllIIIIIIIIlllIl] = IIlIIlIlIlllII[lIIlIIlIllIllI:llIIlIlI]
  elif llIIlllIllIlIlI < llIlIllIIIIIIIIlllIl:
    IllIlIIlllllllll[IllIlIIIlIIIII:llIlIllIIIIIIIIlllIl] = IIlIIlIlIlllII[llIIlllIllIlIlI:llIlIllIIIIIIIIlllIl]
def lIIllIllllIIIIl(IIlIIlIIIIIlIIlIl):
  IlIIlIIllllIIlII = len(IIlIIlIIIIIlIIlIl)
  llIIlIIIllllI = math.ceil(math.log(IlIIlIIllllIIlII,2))
  IIlIIlIlIlllII, IlIlIIlIIIIIIII = IIlIIlIIIIIlIIlIl, [None] * IlIIlIIllllIIlII
  for llllIlllllIlIIIllI in (2**IllllIllIlIllIlIl for IllllIllIlIllIlIl in range(llIIlIIIllllI)):
    for IIIIlllllIl in range(0, IlIIlIIllllIIlII, 2*llllIlllllIlIIIllI):
      IIIIlIlllIIIIllI(IIlIIlIlIlllII, IlIlIIlIIIIIIII, IIIIlllllIl, llllIlllllIlIIIllI)
    IIlIIlIlIlllII, IlIlIIlIIIIIIII = IlIlIIlIIIIIIII, IIlIIlIlIlllII
  if IIlIIlIIIIIlIIlIl is not IIlIIlIlIlllII:
    IIlIIlIIIIIlIIlIl[0:IlIIlIIllllIIlII] = IIlIIlIlIlllII[0:IlIIlIIllllIIlII]