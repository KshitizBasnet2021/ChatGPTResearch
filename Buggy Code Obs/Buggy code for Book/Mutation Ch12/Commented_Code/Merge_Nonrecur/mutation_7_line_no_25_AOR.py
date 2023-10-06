import math
def IllIIllll(IIllIIIlIll, IIIlIlIlIllllI, IllIIIIlIlI, IllIIllIIlIIIlIIIlIl):
  IIlIIllIIIlIllI = IllIIIIlIlI+IllIIllIIlIIIlIIIlIl                        
  lIIIllII = min(IllIIIIlIlI+2*IllIIllIIlIIIlIIIlIl, len(IIllIIIlIll))       
  lIIlIlIlIIllIlIll, IIlllIIIlI, IIllIIllIIlIllllll = IllIIIIlIlI, IllIIIIlIlI+IllIIllIIlIIIlIIIlIl, IllIIIIlIlI       
  while lIIlIlIlIIllIlIll < IIlIIllIIIlIllI and IIlllIIIlI < lIIIllII:
    if IIllIIIlIll[lIIlIlIlIIllIlIll] < IIllIIIlIll[IIlllIIIlI]:
      IIIlIlIlIllllI[IIllIIllIIlIllllll] = IIllIIIlIll[lIIlIlIlIIllIlIll]
      lIIlIlIlIIllIlIll += 1
    else:
      IIIlIlIlIllllI[IIllIIllIIlIllllll] = IIllIIIlIll[IIlllIIIlI]
      IIlllIIIlI += 1
    IIllIIllIIlIllllll += 1                                
  if lIIlIlIlIIllIlIll < IIlIIllIIIlIllI:
    IIIlIlIlIllllI[IIllIIllIIlIllllll:lIIIllII] = IIllIIIlIll[lIIlIlIlIIllIlIll:IIlIIllIIIlIllI]          
  elif IIlllIIIlI < lIIIllII:
    IIIlIlIlIllllI[IIllIIllIIlIllllll:lIIIllII] = IIllIIIlIll[IIlllIIIlI:lIIIllII]          
def lIIIlIlIllIIIIIIlll(lIlIllIl):
  IlllIlIIIIIllIllI = len(lIlIllIl)
  IlIIlllIl = math.ceil(math.log(IlllIlIIIIIllIllI,2))
  (IIllIIIlIll, lIIIlIllIIllIll) = (lIlIllIl, [None] / IlllIlIIIIIllIllI)
  for lIIlIllI in (2**IIllIIlIIIIIl for IIllIIlIIIIIl in range(IlIIlllIl)):   
    for llIIlIllIIIl in range(0, IlllIlIIIIIllIllI, 2*lIIlIllI):            
      IllIIllll(IIllIIIlIll, lIIIlIllIIllIll, llIIlIllIIIl, lIIlIllI)
    IIllIIIlIll, lIIIlIllIIllIll = lIIIlIllIIllIll, IIllIIIlIll                 
  if lIlIllIl is not IIllIIIlIll:
    lIlIllIl[0:IlllIlIIIIIllIllI] = IIllIIIlIll[0:IlllIlIIIIIllIllI]                     