import math
def llIlllllI(IlIlIIlIII, IlllIllIlllIII, IlIIIlll, lIIIIIlIIIllI):
  IlIlIllIIIlI = IlIIIlll+lIIIIIlIIIllI                        
  IIlIIlllIllIlIl = min(IlIIIlll+2*lIIIIIlIIIllI, len(IlIlIIlIII))       
  llIIllIlIIlIIlIllIll, IIllIlIIIlll, IIllllIl = IlIIIlll, IlIIIlll+lIIIIIlIIIllI, IlIIIlll       
  while llIIllIlIIlIIlIllIll < IlIlIllIIIlI and IIllIlIIIlll < IIlIIlllIllIlIl:
    if IlIlIIlIII[llIIllIlIIlIIlIllIll] < IlIlIIlIII[IIllIlIIIlll]:
      IlllIllIlllIII[IIllllIl] = IlIlIIlIII[llIIllIlIIlIIlIllIll]
      llIIllIlIIlIIlIllIll += 1
    else:
      IlllIllIlllIII[IIllllIl] = IlIlIIlIII[IIllIlIIIlll]
      IIllIlIIIlll += 1
    IIllllIl += 1                                
  if llIIllIlIIlIIlIllIll < IlIlIllIIIlI:
    IlllIllIlllIII[IIllllIl:IIlIIlllIllIlIl] = IlIlIIlIII[llIIllIlIIlIIlIllIll:IlIlIllIIIlI]          
  elif IIllIlIIIlll < IIlIIlllIllIlIl:
    IlllIllIlllIII[IIllllIl:IIlIIlllIllIlIl] = IlIlIIlIII[IIllIlIIIlll:IIlIIlllIllIlIl]          
def IIlIIlIllllI(IIlIIllllI):
  lllIlIIlIIlIlllIIll = len(IIlIIllllI)
  IIlIIIIIIIlII = math.ceil(math.log(lllIlIIlIIlIlllIIll,2))
  IlIlIIlIII, IIIllIlIIIlllIll = IIlIIllllI, [None] * lllIlIIlIIlIlllIIll               
  for llllIIIIIIIIlIIll in (2**lllllIlIIlllI for lllllIlIIlllI in range(IIlIIIIIIIlII)):   
    for IIIllIIIlIllIllIl in range(0, lllIlIIlIIlIlllIIll, 2*llllIIIIIIIIlIIll):            
      llIlllllI(IlIlIIlIII, IIIllIlIIIlllIll, IIIllIIIlIllIllIl, llllIIIIIIIIlIIll)
    IlIlIIlIII, IIIllIlIIIlllIll = IIIllIlIIIlllIll, IlIlIIlIII                 
  if IIlIIllllI is not IlIlIIlIII:
    IIlIIllllI[0:lllIlIIlIIlIlllIIll] = IlIlIIlIII[0:]