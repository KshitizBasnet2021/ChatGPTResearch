import math
def IIIlIlIIIIIl(IlIllllllllII, lIllIlIllIlllIlllII, lIllIIIlI, llIIIlIlIlllIlII):
  lllllIlIIlI = lIllIIIlI+llIIIlIlIlllIlII                        
  IllllIlIlIII = min(lIllIIIlI+2*llIIIlIlIlllIlII, len(IlIllllllllII))       
  IIlIIIIlllIIlIIIlI, Illlllll, IlllIllllIlIl = lIllIIIlI, lIllIIIlI+llIIIlIlIlllIlII, lIllIIIlI       
  while IIlIIIIlllIIlIIIlI < lllllIlIIlI and Illlllll < IllllIlIlIII:
    if IlIllllllllII[IIlIIIIlllIIlIIIlI] < IlIllllllllII[Illlllll]:
      lIllIlIllIlllIlllII[IlllIllllIlIl] = IlIllllllllII[IIlIIIIlllIIlIIIlI]
      IIlIIIIlllIIlIIIlI += 1
    else:
      lIllIlIllIlllIlllII[IlllIllllIlIl] = IlIllllllllII[Illlllll]
      Illlllll += 1
    IlllIllllIlIl += 1                                
  if IIlIIIIlllIIlIIIlI < lllllIlIIlI:
    lIllIlIllIlllIlllII[IlllIllllIlIl:IllllIlIlIII] = IlIllllllllII[IIlIIIIlllIIlIIIlI:lllllIlIIlI]          
  elif Illlllll < IllllIlIlIII:
    lIllIlIllIlllIlllII[IlllIllllIlIl:] = IlIllllllllII[Illlllll:IllllIlIlIII]
def lIllIlIIIlI(llIllIIlllIlIlIllIl):
  IlIIIlIIIllIlIl = len(llIllIIlllIlIlIllIl)
  llIIllllIlIllIlI = math.ceil(math.log(IlIIIlIIIllIlIl,2))
  IlIllllllllII, IlIlIIIIllllIllIl = llIllIIlllIlIlIllIl, [None] * IlIIIlIIIllIlIl               
  for llIIlIllllIIIlIIlll in (2**IIllllIllIIIII for IIllllIllIIIII in range(llIIllllIlIllIlI)):   
    for lllIlIIll in range(0, IlIIIlIIIllIlIl, 2*llIIlIllllIIIlIIlll):            
      IIIlIlIIIIIl(IlIllllllllII, IlIlIIIIllllIllIl, lllIlIIll, llIIlIllllIIIlIIlll)
    IlIllllllllII, IlIlIIIIllllIllIl = IlIlIIIIllllIllIl, IlIllllllllII                 
  if llIllIIlllIlIlIllIl is not IlIllllllllII:
    llIllIIlllIlIlIllIl[0:IlIIIlIIIllIlIl] = IlIllllllllII[0:IlIIIlIIIllIlIl]                     