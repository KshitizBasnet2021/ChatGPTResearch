import math
def lllIllllIlllllIIlI(IlIIlIll, lIIIIIIIlIlI, IIIlIlIlIIlllIlll, IIIIllIIll):
  lIlIIIllIIlIIlllIlI = IIIlIlIlIIlllIlll+IIIIllIIll                        
  IIlIlllIIIIlIlI = min(IIIlIlIlIIlllIlll+2*IIIIllIIll, len(IlIIlIll))       
  (lIlIIIll, IlIlIllIIIlIIIll, lIIllIII) = (IIIlIlIlIIlllIlll, IIIlIlIlIIlllIlll - IIIIllIIll, IIIlIlIlIIlllIlll)
  while lIlIIIll < lIlIIIllIIlIIlllIlI and IlIlIllIIIlIIIll < IIlIlllIIIIlIlI:
    if IlIIlIll[lIlIIIll] < IlIIlIll[IlIlIllIIIlIIIll]:
      lIIIIIIIlIlI[lIIllIII] = IlIIlIll[lIlIIIll]
      lIlIIIll += 1
    else:
      lIIIIIIIlIlI[lIIllIII] = IlIIlIll[IlIlIllIIIlIIIll]
      IlIlIllIIIlIIIll += 1
    lIIllIII += 1                                
  if lIlIIIll < lIlIIIllIIlIIlllIlI:
    lIIIIIIIlIlI[lIIllIII:IIlIlllIIIIlIlI] = IlIIlIll[lIlIIIll:lIlIIIllIIlIIlllIlI]          
  elif IlIlIllIIIlIIIll < IIlIlllIIIIlIlI:
    lIIIIIIIlIlI[lIIllIII:IIlIlllIIIIlIlI] = IlIIlIll[IlIlIllIIIlIIIll:IIlIlllIIIIlIlI]          
def IIIllIIllIIIlIlllIl(lIllIIlII):
  llIIIlIIl = len(lIllIIlII)
  lIIIllIIIIlIIIllI = math.ceil(math.log(llIIIlIIl,2))
  IlIIlIll, lIIlllIlIIlIl = lIllIIlII, [None] * llIIIlIIl               
  for IIIlIIIlllI in (2**IIIlIIlIl for IIIlIIlIl in range(lIIIllIIIIlIIIllI)):   
    for IlllIIllII in range(0, llIIIlIIl, 2*IIIlIIIlllI):            
      lllIllllIlllllIIlI(IlIIlIll, lIIlllIlIIlIl, IlllIIllII, IIIlIIIlllI)
    IlIIlIll, lIIlllIlIIlIl = lIIlllIlIIlIl, IlIIlIll                 
  if lIllIIlII is not IlIIlIll:
    lIllIIlII[0:llIIIlIIl] = IlIIlIll[0:llIIIlIIl]                     