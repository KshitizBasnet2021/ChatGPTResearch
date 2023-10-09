import math
def lIlllllIlllIIl(IlIIIllIIIIlIlIllII, lIllIIllIIl, IIIlllIIllIllIlIIlIl, lIlIIIlIllIlIIIIIIl):
  IlIlIIlIl = IIIlllIIllIllIlIIlIl+lIlIIIlIllIlIIIIIIl                        
  lIlIlIllII = min(IIIlllIIllIllIlIIlIl+2*lIlIIIlIllIlIIIIIIl, len(IlIIIllIIIIlIlIllII))       
  IllIIllIIllIIIl, lIllllIIIII, IlllIlIII = IIIlllIIllIllIlIIlIl, IIIlllIIllIllIlIIlIl+lIlIIIlIllIlIIIIIIl, IIIlllIIllIllIlIIlIl       
  while IllIIllIIllIIIl < IlIlIIlIl and lIllllIIIII < lIlIlIllII:
    if not (IlIIIllIIIIlIlIllII[IllIIllIIllIIIl] < IlIIIllIIIIlIlIllII[lIllllIIIII]):
      lIllIIllIIl[IlllIlIII] = IlIIIllIIIIlIlIllII[IllIIllIIllIIIl]
      IllIIllIIllIIIl += 1
    else:
      lIllIIllIIl[IlllIlIII] = IlIIIllIIIIlIlIllII[lIllllIIIII]
      lIllllIIIII += 1
    IlllIlIII += 1                                
  if IllIIllIIllIIIl < IlIlIIlIl:
    lIllIIllIIl[IlllIlIII:lIlIlIllII] = IlIIIllIIIIlIlIllII[IllIIllIIllIIIl:IlIlIIlIl]          
  elif lIllllIIIII < lIlIlIllII:
    lIllIIllIIl[IlllIlIII:lIlIlIllII] = IlIIIllIIIIlIlIllII[lIllllIIIII:lIlIlIllII]          
def IlIIIlIIIIlIIIl(IIlIlIIlIlIIIIlIlIIl):
  lIIIIlllIl = len(IIlIlIIlIlIIIIlIlIIl)
  lIlIIIIlllI = math.ceil(math.log(lIIIIlllIl,2))
  IlIIIllIIIIlIlIllII, llIllllllII = IIlIlIIlIlIIIIlIlIIl, [None] * lIIIIlllIl               
  for llIlIIllI in (2**IlllIllIlllIIlIllIlI for IlllIllIlllIIlIllIlI in range(lIlIIIIlllI)):   
    for lIllllIIIIlIllllIIlI in range(0, lIIIIlllIl, 2*llIlIIllI):            
      lIlllllIlllIIl(IlIIIllIIIIlIlIllII, llIllllllII, lIllllIIIIlIllllIIlI, llIlIIllI)
    IlIIIllIIIIlIlIllII, llIllllllII = llIllllllII, IlIIIllIIIIlIlIllII                 
  if IIlIlIIlIlIIIIlIlIIl is not IlIIIllIIIIlIlIllII:
    IIlIlIIlIlIIIIlIlIIl[0:lIIIIlllIl] = IlIIIllIIIIlIlIllII[0:lIIIIlllIl]                     