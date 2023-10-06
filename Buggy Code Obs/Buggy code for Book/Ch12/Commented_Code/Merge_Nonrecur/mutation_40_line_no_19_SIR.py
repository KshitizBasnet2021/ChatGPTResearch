import math
def lIIIlIIlIl(IIlIllIIIlIIIIllll, IlIlIllIIIlllIll, IIIIlIllIlIll, llllIlIlII):
  llIIllIIlIl = IIIIlIllIlIll+llllIlIlII                        
  IIllIlllII = min(IIIIlIllIlIll+2*llllIlIlII, len(IIlIllIIIlIIIIllll))       
  IIlIlIlllIlllIIl, llIlIIIIIII, llllIlIlIIIll = IIIIlIllIlIll, IIIIlIllIlIll+llllIlIlII, IIIIlIllIlIll       
  while IIlIlIlllIlllIIl < llIIllIIlIl and llIlIIIIIII < IIllIlllII:
    if IIlIllIIIlIIIIllll[IIlIlIlllIlllIIl] < IIlIllIIIlIIIIllll[llIlIIIIIII]:
      IlIlIllIIIlllIll[llllIlIlIIIll] = IIlIllIIIlIIIIllll[IIlIlIlllIlllIIl]
      IIlIlIlllIlllIIl += 1
    else:
      IlIlIllIIIlllIll[llllIlIlIIIll] = IIlIllIIIlIIIIllll[llIlIIIIIII]
      llIlIIIIIII += 1
    llllIlIlIIIll += 1                                
  if IIlIlIlllIlllIIl < llIIllIIlIl:
    IlIlIllIIIlllIll[llllIlIlIIIll:IIllIlllII] = IIlIllIIIlIIIIllll[IIlIlIlllIlllIIl:llIIllIIlIl]          
  elif llIlIIIIIII < IIllIlllII:
    IlIlIllIIIlllIll[llllIlIlIIIll:IIllIlllII] = IIlIllIIIlIIIIllll[llIlIIIIIII:]
def IlIIIIIIll(IlIIlIIIllllIlIllIIl):
  lIlllIIIIlIllIl = len(IlIIlIIIllllIlIllIIl)
  IIllIlIIlII = math.ceil(math.log(lIlllIIIIlIllIl,2))
  IIlIllIIIlIIIIllll, IIIIIIIIlIIIllI = IlIIlIIIllllIlIllIIl, [None] * lIlllIIIIlIllIl               
  for llIlIlIlIllllllIllII in (2**IIIlIlllIIlIIIIl for IIIlIlllIIlIIIIl in range(IIllIlIIlII)):   
    for IIlllIIIlIlllllIIll in range(0, lIlllIIIIlIllIl, 2*llIlIlIlIllllllIllII):            
      lIIIlIIlIl(IIlIllIIIlIIIIllll, IIIIIIIIlIIIllI, IIlllIIIlIlllllIIll, llIlIlIlIllllllIllII)
    IIlIllIIIlIIIIllll, IIIIIIIIlIIIllI = IIIIIIIIlIIIllI, IIlIllIIIlIIIIllll                 
  if IlIIlIIIllllIlIllIIl is not IIlIllIIIlIIIIllll:
    IlIIlIIIllllIlIllIIl[0:lIlllIIIIlIllIl] = IIlIllIIIlIIIIllll[0:lIlllIIIIlIllIl]                     