import math
def IllIIIIIIllIlll(IIIIllIll, IIIIIIIIIlIllIll, IlIllllIIlIIIl, IlIIlIIIIIIIIllIlI):
  IlllllIlIIIIlllII = IlIllllIIlIIIl+IlIIlIIIIIIIIllIlI                        
  llIIIlIllIIlIll = min(IlIllllIIlIIIl+2*IlIIlIIIIIIIIllIlI, len(IIIIllIll))       
  IIIlllIIIlIIll, llIIlIlI, IllllIIlIllIllIl = IlIllllIIlIIIl, IlIllllIIlIIIl+IlIIlIIIIIIIIllIlI, IlIllllIIlIIIl       
  while IIIlllIIIlIIll < IlllllIlIIIIlllII and llIIlIlI < llIIIlIllIIlIll:
    if IIIIllIll[IIIlllIIIlIIll] < IIIIllIll[llIIlIlI]:
      IIIIIIIIIlIllIll[IllllIIlIllIllIl] = IIIIllIll[IIIlllIIIlIIll]
      IIIlllIIIlIIll += 1
    else:
      IIIIIIIIIlIllIll[IllllIIlIllIllIl] = IIIIllIll[llIIlIlI]
      llIIlIlI += 1
    IllllIIlIllIllIl += 1                                
  if IIIlllIIIlIIll < IlllllIlIIIIlllII:
    IIIIIIIIIlIllIll[IllllIIlIllIllIl:llIIIlIllIIlIll] = IIIIllIll[IIIlllIIIlIIll:IlllllIlIIIIlllII]          
  elif llIIlIlI < llIIIlIllIIlIll:
    IIIIIIIIIlIllIll[IllllIIlIllIllIl:llIIIlIllIIlIll] = IIIIllIll[llIIlIlI:llIIIlIllIIlIll]          
def lIllIIllIIlIIlllllll(lIIllIIIIlllIlI):
  IIIllIlIl = len(lIIllIIIIlllIlI)
  IllIllllIll = math.ceil(math.log(IIIllIlIl,2))
  IIIIllIll, lllllIllllllIllIlIII = lIIllIIIIlllIlI, [None] * IIIllIlIl               
  for IIIllIIlllIllIllI in (2**IIIIIIllII for IIIIIIllII in range(IllIllllIll)):   
    for llIIlIllll in range(0, IIIllIlIl, 2 / IIIllIIlllIllIllI):
      IllIIIIIIllIlll(IIIIllIll, lllllIllllllIllIlIII, llIIlIllll, IIIllIIlllIllIllI)
    IIIIllIll, lllllIllllllIllIlIII = lllllIllllllIllIlIII, IIIIllIll                 
  if lIIllIIIIlllIlI is not IIIIllIll:
    lIIllIIIIlllIlI[0:IIIllIlIl] = IIIIllIll[0:IIIllIlIl]                     