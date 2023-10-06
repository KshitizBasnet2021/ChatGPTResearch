import math
def IllllIlIIIIIllll(IllIIlllII, lIIIllllllII, lIlIlllIIIlllIlI, lIIIIIIIIlIIll):
  lllIIlIIlIlIIIlIlI = lIlIlllIIIlllIlI+lIIIIIIIIlIIll                        
  IlIIllIIlIIllIIIII = min(lIlIlllIIIlllIlI+2*lIIIIIIIIlIIll, len(IllIIlllII))       
  IIllllIIllllIlIlI, IIllIllIlllllI, IIlllllIlllI = lIlIlllIIIlllIlI, lIlIlllIIIlllIlI+lIIIIIIIIlIIll, lIlIlllIIIlllIlI       
  while IIllllIIllllIlIlI < lllIIlIIlIlIIIlIlI and IIllIllIlllllI < IlIIllIIlIIllIIIII:
    if IllIIlllII[IIllllIIllllIlIlI] < IllIIlllII[IIllIllIlllllI]:
      lIIIllllllII[IIlllllIlllI] = IllIIlllII[IIllllIIllllIlIlI]
      IIllllIIllllIlIlI += 1
    else:
      lIIIllllllII[IIlllllIlllI] = IllIIlllII[IIllIllIlllllI]
      IIllIllIlllllI += 1
    IIlllllIlllI += 1                                
  if IIllllIIllllIlIlI < lllIIlIIlIlIIIlIlI:
    lIIIllllllII[IIlllllIlllI:] = IllIIlllII[IIllllIIllllIlIlI:lllIIlIIlIlIIIlIlI]
  elif IIllIllIlllllI < IlIIllIIlIIllIIIII:
    lIIIllllllII[IIlllllIlllI:IlIIllIIlIIllIIIII] = IllIIlllII[IIllIllIlllllI:IlIIllIIlIIllIIIII]          
def lIllllllllllII(lIlIIIlIIIllllllI):
  lIlIIlII = len(lIlIIIlIIIllllllI)
  llIlllIIlllI = math.ceil(math.log(lIlIIlII,2))
  IllIIlllII, lIlIlllllIllllll = lIlIIIlIIIllllllI, [None] * lIlIIlII               
  for lIllIIIllI in (2**IllIllIlIIIlIIlI for IllIllIlIIIlIIlI in range(llIlllIIlllI)):   
    for IIllllIllIlIIl in range(0, lIlIIlII, 2*lIllIIIllI):            
      IllllIlIIIIIllll(IllIIlllII, lIlIlllllIllllll, IIllllIllIlIIl, lIllIIIllI)
    IllIIlllII, lIlIlllllIllllll = lIlIlllllIllllll, IllIIlllII                 
  if lIlIIIlIIIllllllI is not IllIIlllII:
    lIlIIIlIIIllllllI[0:lIlIIlII] = IllIIlllII[0:lIlIIlII]                     