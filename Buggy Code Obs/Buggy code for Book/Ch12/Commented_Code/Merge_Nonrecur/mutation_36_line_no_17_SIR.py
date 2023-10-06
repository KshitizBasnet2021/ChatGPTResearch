import math
def lIlIllIllIII(IIIlIlIIIIlIII, lIIlIllIl, lIllIllIlllllIIllll, IIIIIlIIIllIll):
  IlIlllIIll = lIllIllIlllllIIllll+IIIIIlIIIllIll                        
  lIIIIIlllIII = min(lIllIllIlllllIIllll+2*IIIIIlIIIllIll, len(IIIlIlIIIIlIII))       
  llIllIIIlIll, IIIlIllIIlIlIlllIlIl, lIIlIlII = lIllIllIlllllIIllll, lIllIllIlllllIIllll+IIIIIlIIIllIll, lIllIllIlllllIIllll       
  while llIllIIIlIll < IlIlllIIll and IIIlIllIIlIlIlllIlIl < lIIIIIlllIII:
    if IIIlIlIIIIlIII[llIllIIIlIll] < IIIlIlIIIIlIII[IIIlIllIIlIlIlllIlIl]:
      lIIlIllIl[lIIlIlII] = IIIlIlIIIIlIII[llIllIIIlIll]
      llIllIIIlIll += 1
    else:
      lIIlIllIl[lIIlIlII] = IIIlIlIIIIlIII[IIIlIllIIlIlIlllIlIl]
      IIIlIllIIlIlIlllIlIl += 1
    lIIlIlII += 1                                
  if llIllIIIlIll < IlIlllIIll:
    lIIlIllIl[lIIlIlII:lIIIIIlllIII] = IIIlIlIIIIlIII[llIllIIIlIll:]
  elif IIIlIllIIlIlIlllIlIl < lIIIIIlllIII:
    lIIlIllIl[lIIlIlII:lIIIIIlllIII] = IIIlIlIIIIlIII[IIIlIllIIlIlIlllIlIl:lIIIIIlllIII]          
def lIIIlIIIlllIIlIIIl(IlIIllIlIllIlI):
  IllIIIlIIIl = len(IlIIllIlIllIlI)
  IlIlIIIIIII = math.ceil(math.log(IllIIIlIIIl,2))
  IIIlIlIIIIlIII, lIIIlIIlIlII = IlIIllIlIllIlI, [None] * IllIIIlIIIl               
  for llIIIlIIlIlIllll in (2**lIIlIIlIIlllIIlIll for lIIlIIlIIlllIIlIll in range(IlIlIIIIIII)):   
    for llIIIIlIIIIIIlllI in range(0, IllIIIlIIIl, 2*llIIIlIIlIlIllll):            
      lIlIllIllIII(IIIlIlIIIIlIII, lIIIlIIlIlII, llIIIIlIIIIIIlllI, llIIIlIIlIlIllll)
    IIIlIlIIIIlIII, lIIIlIIlIlII = lIIIlIIlIlII, IIIlIlIIIIlIII                 
  if IlIIllIlIllIlI is not IIIlIlIIIIlIII:
    IlIIllIlIllIlI[0:IllIIIlIIIl] = IIIlIlIIIIlIII[0:IllIIIlIIIl]                     