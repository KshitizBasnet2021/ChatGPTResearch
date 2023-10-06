import math
def llIlIlllIIl(lIIIIlIlIlIIlII, IIIIlIllIIllllllI, IIlIIlllIIlI, lIlIllIIIl):
  lllIlIllllIIIlllIl = IIlIIlllIIlI - lIlIllIIIl
  IIIllIllIlIlIIIIIl = min(IIlIIlllIIlI+2*lIlIllIIIl, len(lIIIIlIlIlIIlII))       
  llIIIIlIIllIlII, lIIllIllIIIllllIlIII, IlIlIlllIIIII = IIlIIlllIIlI, IIlIIlllIIlI+lIlIllIIIl, IIlIIlllIIlI       
  while llIIIIlIIllIlII < lllIlIllllIIIlllIl and lIIllIllIIIllllIlIII < IIIllIllIlIlIIIIIl:
    if lIIIIlIlIlIIlII[llIIIIlIIllIlII] < lIIIIlIlIlIIlII[lIIllIllIIIllllIlIII]:
      IIIIlIllIIllllllI[IlIlIlllIIIII] = lIIIIlIlIlIIlII[llIIIIlIIllIlII]
      llIIIIlIIllIlII += 1
    else:
      IIIIlIllIIllllllI[IlIlIlllIIIII] = lIIIIlIlIlIIlII[lIIllIllIIIllllIlIII]
      lIIllIllIIIllllIlIII += 1
    IlIlIlllIIIII += 1                                
  if llIIIIlIIllIlII < lllIlIllllIIIlllIl:
    IIIIlIllIIllllllI[IlIlIlllIIIII:IIIllIllIlIlIIIIIl] = lIIIIlIlIlIIlII[llIIIIlIIllIlII:lllIlIllllIIIlllIl]          
  elif lIIllIllIIIllllIlIII < IIIllIllIlIlIIIIIl:
    IIIIlIllIIllllllI[IlIlIlllIIIII:IIIllIllIlIlIIIIIl] = lIIIIlIlIlIIlII[lIIllIllIIIllllIlIII:IIIllIllIlIlIIIIIl]          
def IIlIllllI(IllIlIllIlllIIIllIll):
  lIIllIllllIIIllII = len(IllIlIllIlllIIIllIll)
  IIIIllIIlI = math.ceil(math.log(lIIllIllllIIIllII,2))
  lIIIIlIlIlIIlII, lIIIIIII = IllIlIllIlllIIIllIll, [None] * lIIllIllllIIIllII               
  for IlIlIIIIIIlllllIlIl in (2**IllIIIllll for IllIIIllll in range(IIIIllIIlI)):   
    for lllIllIllIII in range(0, lIIllIllllIIIllII, 2*IlIlIIIIIIlllllIlIl):            
      llIlIlllIIl(lIIIIlIlIlIIlII, lIIIIIII, lllIllIllIII, IlIlIIIIIIlllllIlIl)
    lIIIIlIlIlIIlII, lIIIIIII = lIIIIIII, lIIIIlIlIlIIlII                 
  if IllIlIllIlllIIIllIll is not lIIIIlIlIlIIlII:
    IllIlIllIlllIIIllIll[0:lIIllIllllIIIllII] = lIIIIlIlIlIIlII[0:lIIllIllllIIIllII]                     