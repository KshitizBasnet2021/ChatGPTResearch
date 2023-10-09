import math
def llIIIIIIIIIIIIllIl(llIIlIIl, IIllIIIII, IlIlIIIIll, lIIIIIIllIIIlIlIlll):
  IIIIllIIIIllIlllII = IlIlIIIIll+lIIIIIIllIIIlIlIlll                        
  IIllIIllIllIllIIIII = min(IlIlIIIIll+2*lIIIIIIllIIIlIlIlll, len(llIIlIIl))       
  IIllIIIIlIlIllllIlIl, IllIlIllllIIIIlI, IlllIlIIl = IlIlIIIIll, IlIlIIIIll+lIIIIIIllIIIlIlIlll, IlIlIIIIll       
  while IIllIIIIlIlIllllIlIl < IIIIllIIIIllIlllII and IllIlIllllIIIIlI < IIllIIllIllIllIIIII:
    if llIIlIIl[IIllIIIIlIlIllllIlIl] < llIIlIIl[IllIlIllllIIIIlI]:
      IIllIIIII[IlllIlIIl] = llIIlIIl[IIllIIIIlIlIllllIlIl]
      IIllIIIIlIlIllllIlIl += 1
    else:
      IIllIIIII[IlllIlIIl] = llIIlIIl[IllIlIllllIIIIlI]
      IllIlIllllIIIIlI += 1
    IlllIlIIl += 1                                
  if IIllIIIIlIlIllllIlIl < IIIIllIIIIllIlllII:
    IIllIIIII[IlllIlIIl:IIllIIllIllIllIIIII] = llIIlIIl[:IIIIllIIIIllIlllII]
  elif IllIlIllllIIIIlI < IIllIIllIllIllIIIII:
    IIllIIIII[IlllIlIIl:IIllIIllIllIllIIIII] = llIIlIIl[IllIlIllllIIIIlI:IIllIIllIllIllIIIII]          
def IIllllIlIl(IlllllIIIllIIlIIIIl):
  lIIIllIIlIIIIIII = len(IlllllIIIllIIlIIIIl)
  IllllIIlIlIII = math.ceil(math.log(lIIIllIIlIIIIIII,2))
  llIIlIIl, IIlIlIll = IlllllIIIllIIlIIIIl, [None] * lIIIllIIlIIIIIII               
  for IllIIllllI in (2**lIlIIlIII for lIlIIlIII in range(IllllIIlIlIII)):   
    for IlIllIIIIIIIlIIIlll in range(0, lIIIllIIlIIIIIII, 2*IllIIllllI):            
      llIIIIIIIIIIIIllIl(llIIlIIl, IIlIlIll, IlIllIIIIIIIlIIIlll, IllIIllllI)
    llIIlIIl, IIlIlIll = IIlIlIll, llIIlIIl                 
  if IlllllIIIllIIlIIIIl is not llIIlIIl:
    IlllllIIIllIIlIIIIl[0:lIIIllIIlIIIIIII] = llIIlIIl[0:lIIIllIIlIIIIIII]                     