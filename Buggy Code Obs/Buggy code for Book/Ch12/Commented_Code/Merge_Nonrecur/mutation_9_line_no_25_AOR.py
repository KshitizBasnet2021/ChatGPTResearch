import math
def IlIIIlIl(IIIllIIlI, IlIllIIIlIlllIIlIl, lllIIlIIl, IlIlIlIIllII):
  IlIllllI = lllIIlIIl+IlIlIlIIllII                        
  lIIlllIlIIIIIIlI = min(lllIIlIIl+2*IlIlIlIIllII, len(IIIllIIlI))       
  lIllIIIIllllIlII, llIlllIIIlIlllIlI, IIllIllIIIllIlI = lllIIlIIl, lllIIlIIl+IlIlIlIIllII, lllIIlIIl       
  while lIllIIIIllllIlII < IlIllllI and llIlllIIIlIlllIlI < lIIlllIlIIIIIIlI:
    if IIIllIIlI[lIllIIIIllllIlII] < IIIllIIlI[llIlllIIIlIlllIlI]:
      IlIllIIIlIlllIIlIl[IIllIllIIIllIlI] = IIIllIIlI[lIllIIIIllllIlII]
      lIllIIIIllllIlII += 1
    else:
      IlIllIIIlIlllIIlIl[IIllIllIIIllIlI] = IIIllIIlI[llIlllIIIlIlllIlI]
      llIlllIIIlIlllIlI += 1
    IIllIllIIIllIlI += 1                                
  if lIllIIIIllllIlII < IlIllllI:
    IlIllIIIlIlllIIlIl[IIllIllIIIllIlI:lIIlllIlIIIIIIlI] = IIIllIIlI[lIllIIIIllllIlII:IlIllllI]          
  elif llIlllIIIlIlllIlI < lIIlllIlIIIIIIlI:
    IlIllIIIlIlllIIlIl[IIllIllIIIllIlI:lIIlllIlIIIIIIlI] = IIIllIIlI[llIlllIIIlIlllIlI:lIIlllIlIIIIIIlI]          
def IlIIlIlIlllI(lIllIlIllllllll):
  llIllIIIIIlllI = len(lIllIlIllllllll)
  lIllIllIIII = math.ceil(math.log(llIllIIIIIlllI,2))
  (IIIllIIlI, lIlIIllll) = (lIllIlIllllllll, [None] ** llIllIIIIIlllI)
  for IllIIIllllIlIl in (2**IlllIIllIl for IlllIIllIl in range(lIllIllIIII)):   
    for lllIIllIIIIIlIlllII in range(0, llIllIIIIIlllI, 2*IllIIIllllIlIl):            
      IlIIIlIl(IIIllIIlI, lIlIIllll, lllIIllIIIIIlIlllII, IllIIIllllIlIl)
    IIIllIIlI, lIlIIllll = lIlIIllll, IIIllIIlI                 
  if lIllIlIllllllll is not IIIllIIlI:
    lIllIlIllllllll[0:llIllIIIIIlllI] = IIIllIIlI[0:llIllIIIIIlllI]                     