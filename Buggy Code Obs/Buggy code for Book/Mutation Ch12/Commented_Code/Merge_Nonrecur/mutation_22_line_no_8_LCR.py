import math
def IlIIllIlllIIIII(IIllIllllIIIIlIllIII, llIIllllIl, llllIIlIlIlI, lIllllll):
  IlIIlIlIllll = llllIIlIlIlI+lIllllll                        
  IIlIlIIIIIllII = min(llllIIlIlIlI+2*lIllllll, len(IIllIllllIIIIlIllIII))       
  lIlllIIl, IIIlIIIIll, IlIlllIIIlIlIl = llllIIlIlIlI, llllIIlIlIlI+lIllllll, llllIIlIlIlI       
  while (lIlllIIl < IlIIlIlIllll or IIIlIIIIll < IIlIlIIIIIllII):
    if IIllIllllIIIIlIllIII[lIlllIIl] < IIllIllllIIIIlIllIII[IIIlIIIIll]:
      llIIllllIl[IlIlllIIIlIlIl] = IIllIllllIIIIlIllIII[lIlllIIl]
      lIlllIIl += 1
    else:
      llIIllllIl[IlIlllIIIlIlIl] = IIllIllllIIIIlIllIII[IIIlIIIIll]
      IIIlIIIIll += 1
    IlIlllIIIlIlIl += 1                                
  if lIlllIIl < IlIIlIlIllll:
    llIIllllIl[IlIlllIIIlIlIl:IIlIlIIIIIllII] = IIllIllllIIIIlIllIII[lIlllIIl:IlIIlIlIllll]          
  elif IIIlIIIIll < IIlIlIIIIIllII:
    llIIllllIl[IlIlllIIIlIlIl:IIlIlIIIIIllII] = IIllIllllIIIIlIllIII[IIIlIIIIll:IIlIlIIIIIllII]          
def IlIIIlIIllIII(IIIIIIllIIIIIIllIlI):
  IIlllIlllIlIlll = len(IIIIIIllIIIIIIllIlI)
  IlIIIIIIlIIlIII = math.ceil(math.log(IIlllIlllIlIlll,2))
  IIllIllllIIIIlIllIII, IlIlIllII = IIIIIIllIIIIIIllIlI, [None] * IIlllIlllIlIlll               
  for IlIlllIIIlllIIIlI in (2**IlllIllllIIlll for IlllIllllIIlll in range(IlIIIIIIlIIlIII)):   
    for IlIlllIlIllIlIllll in range(0, IIlllIlllIlIlll, 2*IlIlllIIIlllIIIlI):            
      IlIIllIlllIIIII(IIllIllllIIIIlIllIII, IlIlIllII, IlIlllIlIllIlIllll, IlIlllIIIlllIIIlI)
    IIllIllllIIIIlIllIII, IlIlIllII = IlIlIllII, IIllIllllIIIIlIllIII                 
  if IIIIIIllIIIIIIllIlI is not IIllIllllIIIIlIllIII:
    IIIIIIllIIIIIIllIlI[0:IIlllIlllIlIlll] = IIllIllllIIIIlIllIII[0:IIlllIlllIlIlll]                     