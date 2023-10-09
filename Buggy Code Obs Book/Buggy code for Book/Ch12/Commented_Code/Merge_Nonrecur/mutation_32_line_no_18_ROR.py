import math
def IllIIlllIIllllI(lIIlIllIIlllIIl, IllIIlIIIlIlllIllIlI, IlIIIIIIIllIlIIlIlIl, llIIIIllIllIlIll):
  llIllIIllIIIlllIIlII = IlIIIIIIIllIlIIlIlIl+llIIIIllIllIlIll                        
  IlIlIIIIlI = min(IlIIIIIIIllIlIIlIlIl+2*llIIIIllIllIlIll, len(lIIlIllIIlllIIl))       
  lIIlllllIIlIII, lIlIIIlll, lIIIllllIIllIlIIIlI = IlIIIIIIIllIlIIlIlIl, IlIIIIIIIllIlIIlIlIl+llIIIIllIllIlIll, IlIIIIIIIllIlIIlIlIl       
  while lIIlllllIIlIII < llIllIIllIIIlllIIlII and lIlIIIlll < IlIlIIIIlI:
    if lIIlIllIIlllIIl[lIIlllllIIlIII] < lIIlIllIIlllIIl[lIlIIIlll]:
      IllIIlIIIlIlllIllIlI[lIIIllllIIllIlIIIlI] = lIIlIllIIlllIIl[lIIlllllIIlIII]
      lIIlllllIIlIII += 1
    else:
      IllIIlIIIlIlllIllIlI[lIIIllllIIllIlIIIlI] = lIIlIllIIlllIIl[lIlIIIlll]
      lIlIIIlll += 1
    lIIIllllIIllIlIIIlI += 1                                
  if lIIlllllIIlIII < llIllIIllIIIlllIIlII:
    IllIIlIIIlIlllIllIlI[lIIIllllIIllIlIIIlI:IlIlIIIIlI] = lIIlIllIIlllIIl[lIIlllllIIlIII:llIllIIllIIIlllIIlII]          
  elif lIlIIIlll <= IlIlIIIIlI:
    IllIIlIIIlIlllIllIlI[lIIIllllIIllIlIIIlI:IlIlIIIIlI] = lIIlIllIIlllIIl[lIlIIIlll:IlIlIIIIlI]          
def llIIIIlllIIlIl(IlIlIIIII):
  lIllllII = len(IlIlIIIII)
  IlIlIIlIlIIlIlIll = math.ceil(math.log(lIllllII,2))
  lIIlIllIIlllIIl, IIIIIlIllIIII = IlIlIIIII, [None] * lIllllII               
  for IIlIIIIlllIIlII in (2**llIlIlllIllllIIIll for llIlIlllIllllIIIll in range(IlIlIIlIlIIlIlIll)):   
    for IIlllIlllIlIlllIl in range(0, lIllllII, 2*IIlIIIIlllIIlII):            
      IllIIlllIIllllI(lIIlIllIIlllIIl, IIIIIlIllIIII, IIlllIlllIlIlllIl, IIlIIIIlllIIlII)
    lIIlIllIIlllIIl, IIIIIlIllIIII = IIIIIlIllIIII, lIIlIllIIlllIIl                 
  if IlIlIIIII is not lIIlIllIIlllIIl:
    IlIlIIIII[0:lIllllII] = lIIlIllIIlllIIl[0:lIllllII]                     