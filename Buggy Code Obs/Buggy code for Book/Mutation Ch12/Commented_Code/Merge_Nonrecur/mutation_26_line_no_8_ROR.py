import math
def llIlllIllIllllIIIlIl(lIIlIIIlllllIIlIl, IIlllllllIIlI, lIllIIlIllllll, lIlIlIlI):
  IllIlIII = lIllIIlIllllll+lIlIlIlI                        
  IIlIIlll = min(lIllIIlIllllll+2*lIlIlIlI, len(lIIlIIIlllllIIlIl))       
  IIIIIlIIlIII, IIllIIIIIIIIIIIII, IlIlIIIIIl = lIllIIlIllllll, lIllIIlIllllll+lIlIlIlI, lIllIIlIllllll       
  while (IIIIIlIIlIII < IllIlIII and IIllIIIIIIIIIIIII <= IIlIIlll):
    if lIIlIIIlllllIIlIl[IIIIIlIIlIII] < lIIlIIIlllllIIlIl[IIllIIIIIIIIIIIII]:
      IIlllllllIIlI[IlIlIIIIIl] = lIIlIIIlllllIIlIl[IIIIIlIIlIII]
      IIIIIlIIlIII += 1
    else:
      IIlllllllIIlI[IlIlIIIIIl] = lIIlIIIlllllIIlIl[IIllIIIIIIIIIIIII]
      IIllIIIIIIIIIIIII += 1
    IlIlIIIIIl += 1                                
  if IIIIIlIIlIII < IllIlIII:
    IIlllllllIIlI[IlIlIIIIIl:IIlIIlll] = lIIlIIIlllllIIlIl[IIIIIlIIlIII:IllIlIII]          
  elif IIllIIIIIIIIIIIII < IIlIIlll:
    IIlllllllIIlI[IlIlIIIIIl:IIlIIlll] = lIIlIIIlllllIIlIl[IIllIIIIIIIIIIIII:IIlIIlll]          
def IllIlIIIllIIIlllI(IlIIIlIllIllIll):
  IIlIIllIlllIlIllI = len(IlIIIlIllIllIll)
  lIllIIIII = math.ceil(math.log(IIlIIllIlllIlIllI,2))
  lIIlIIIlllllIIlIl, IIlIlIIIllllIIIIllI = IlIIIlIllIllIll, [None] * IIlIIllIlllIlIllI               
  for IlIIIlIl in (2**llIIlllIlIlll for llIIlllIlIlll in range(lIllIIIII)):   
    for IIllIIllIllIllllIll in range(0, IIlIIllIlllIlIllI, 2*IlIIIlIl):            
      llIlllIllIllllIIIlIl(lIIlIIIlllllIIlIl, IIlIlIIIllllIIIIllI, IIllIIllIllIllllIll, IlIIIlIl)
    lIIlIIIlllllIIlIl, IIlIlIIIllllIIIIllI = IIlIlIIIllllIIIIllI, lIIlIIIlllllIIlIl                 
  if IlIIIlIllIllIll is not lIIlIIIlllllIIlIl:
    IlIIIlIllIllIll[0:IIlIIllIlllIlIllI] = lIIlIIIlllllIIlIl[0:IIlIIllIlllIlIllI]                     