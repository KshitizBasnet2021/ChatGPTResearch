import math
def IlIlIlIlIllIlIlIlI(IlIIIIIlllllIIll, llIllIlIIlllIIIlII, IlIIlIlll, IllIIIlIIllll):
  IIlllIIlIllllIIllIII = IlIIlIlll+IllIIIlIIllll                        
  lIlIlIlIll = min(IlIIlIlll+2*IllIIIlIIllll, len(IlIIIIIlllllIIll))       
  llllIllllllll, IIIllIllIlIlIlllI, llIlIllllIIIIIl = IlIIlIlll, IlIIlIlll+IllIIIlIIllll, IlIIlIlll       
  while not ((llllIllllllll < IIlllIIlIllllIIllIII and IIIllIllIlIlIlllI < lIlIlIlIll)):
    if IlIIIIIlllllIIll[llllIllllllll] < IlIIIIIlllllIIll[IIIllIllIlIlIlllI]:
      llIllIlIIlllIIIlII[llIlIllllIIIIIl] = IlIIIIIlllllIIll[llllIllllllll]
      llllIllllllll += 1
    else:
      llIllIlIIlllIIIlII[llIlIllllIIIIIl] = IlIIIIIlllllIIll[IIIllIllIlIlIlllI]
      IIIllIllIlIlIlllI += 1
    llIlIllllIIIIIl += 1                                
  if llllIllllllll < IIlllIIlIllllIIllIII:
    llIllIlIIlllIIIlII[llIlIllllIIIIIl:lIlIlIlIll] = IlIIIIIlllllIIll[llllIllllllll:IIlllIIlIllllIIllIII]          
  elif IIIllIllIlIlIlllI < lIlIlIlIll:
    llIllIlIIlllIIIlII[llIlIllllIIIIIl:lIlIlIlIll] = IlIIIIIlllllIIll[IIIllIllIlIlIlllI:lIlIlIlIll]          
def llllllIIlIllI(llIlllIllllIIlII):
  IIllIIIlllllIlIIlIII = len(llIlllIllllIIlII)
  llIllIllllllllIIlII = math.ceil(math.log(IIllIIIlllllIlIIlIII,2))
  IlIIIIIlllllIIll, lIllIIlIllII = llIlllIllllIIlII, [None] * IIllIIIlllllIlIIlIII               
  for IllIIlIIIIllII in (2**llllIIlIl for llllIIlIl in range(llIllIllllllllIIlII)):   
    for lIIIlllIllIIIIllIIIl in range(0, IIllIIIlllllIlIIlIII, 2*IllIIlIIIIllII):            
      IlIlIlIlIllIlIlIlI(IlIIIIIlllllIIll, lIllIIlIllII, lIIIlllIllIIIIllIIIl, IllIIlIIIIllII)
    IlIIIIIlllllIIll, lIllIIlIllII = lIllIIlIllII, IlIIIIIlllllIIll                 
  if llIlllIllllIIlII is not IlIIIIIlllllIIll:
    llIlllIllllIIlII[0:IIllIIIlllllIlIIlIII] = IlIIIIIlllllIIll[0:IIllIIIlllllIlIIlIII]                     