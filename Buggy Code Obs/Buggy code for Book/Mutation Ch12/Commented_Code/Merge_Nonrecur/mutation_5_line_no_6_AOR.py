import math
def lIllIllII(llIlIIIIllIIlIllIlII, IlIIIIlIIlIIlIIl, IIlIIIIIlIlIllIIlll, llllIIIl):
  IllllllIIllI = IIlIIIIIlIlIllIIlll+llllIIIl                        
  IlIIIIlIllIlIl = min(IIlIIIIIlIlIllIIlll + (2 ** llllIIIl), len(llIlIIIIllIIlIllIlII))
  llIIlllIllI, lIIIIIIlIIIIIllIlIlI, lIIIIlllIlIllIIlIlIl = IIlIIIIIlIlIllIIlll, IIlIIIIIlIlIllIIlll+llllIIIl, IIlIIIIIlIlIllIIlll       
  while llIIlllIllI < IllllllIIllI and lIIIIIIlIIIIIllIlIlI < IlIIIIlIllIlIl:
    if llIlIIIIllIIlIllIlII[llIIlllIllI] < llIlIIIIllIIlIllIlII[lIIIIIIlIIIIIllIlIlI]:
      IlIIIIlIIlIIlIIl[lIIIIlllIlIllIIlIlIl] = llIlIIIIllIIlIllIlII[llIIlllIllI]
      llIIlllIllI += 1
    else:
      IlIIIIlIIlIIlIIl[lIIIIlllIlIllIIlIlIl] = llIlIIIIllIIlIllIlII[lIIIIIIlIIIIIllIlIlI]
      lIIIIIIlIIIIIllIlIlI += 1
    lIIIIlllIlIllIIlIlIl += 1                                
  if llIIlllIllI < IllllllIIllI:
    IlIIIIlIIlIIlIIl[lIIIIlllIlIllIIlIlIl:IlIIIIlIllIlIl] = llIlIIIIllIIlIllIlII[llIIlllIllI:IllllllIIllI]          
  elif lIIIIIIlIIIIIllIlIlI < IlIIIIlIllIlIl:
    IlIIIIlIIlIIlIIl[lIIIIlllIlIllIIlIlIl:IlIIIIlIllIlIl] = llIlIIIIllIIlIllIlII[lIIIIIIlIIIIIllIlIlI:IlIIIIlIllIlIl]          
def IIIIlIIIlIlI(lIIIIIIl):
  lIlIlIIlIIlllllllIll = len(lIIIIIIl)
  llIllllIlIIII = math.ceil(math.log(lIlIlIIlIIlllllllIll,2))
  llIlIIIIllIIlIllIlII, IIlIlIIlIIllIlllIII = lIIIIIIl, [None] * lIlIlIIlIIlllllllIll               
  for lIIlIllllIIlIIll in (2**llIIlIIIIlIIlIlll for llIIlIIIIlIIlIlll in range(llIllllIlIIII)):   
    for llIIlllIll in range(0, lIlIlIIlIIlllllllIll, 2*lIIlIllllIIlIIll):            
      lIllIllII(llIlIIIIllIIlIllIlII, IIlIlIIlIIllIlllIII, llIIlllIll, lIIlIllllIIlIIll)
    llIlIIIIllIIlIllIlII, IIlIlIIlIIllIlllIII = IIlIlIIlIIllIlllIII, llIlIIIIllIIlIllIlII                 
  if lIIIIIIl is not llIlIIIIllIIlIllIlII:
    lIIIIIIl[0:lIlIlIIlIIlllllllIll] = llIlIIIIllIIlIllIlII[0:lIlIlIIlIIlllllllIll]                     