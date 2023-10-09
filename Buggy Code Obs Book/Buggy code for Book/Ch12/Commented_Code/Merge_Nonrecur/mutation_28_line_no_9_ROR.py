import math
def IlIIIllIl(lllIlIlIlllllllll, IlIIIIlIIIlIIIl, llIIlIlIlIIlll, lIIIlIlI):
  IlllllII = llIIlIlIlIIlll+lIIIlIlI                        
  lIIIllIlII = min(llIIlIlIlIIlll+2*lIIIlIlI, len(lllIlIlIlllllllll))       
  IIIIlIllIIlI, llllIllIII, IlIIllIlIlIIlIIIllI = llIIlIlIlIIlll, llIIlIlIlIIlll+lIIIlIlI, llIIlIlIlIIlll       
  while IIIIlIllIIlI < IlllllII and llllIllIII < lIIIllIlII:
    if lllIlIlIlllllllll[IIIIlIllIIlI] <= lllIlIlIlllllllll[llllIllIII]:
      IlIIIIlIIIlIIIl[IlIIllIlIlIIlIIIllI] = lllIlIlIlllllllll[IIIIlIllIIlI]
      IIIIlIllIIlI += 1
    else:
      IlIIIIlIIIlIIIl[IlIIllIlIlIIlIIIllI] = lllIlIlIlllllllll[llllIllIII]
      llllIllIII += 1
    IlIIllIlIlIIlIIIllI += 1                                
  if IIIIlIllIIlI < IlllllII:
    IlIIIIlIIIlIIIl[IlIIllIlIlIIlIIIllI:lIIIllIlII] = lllIlIlIlllllllll[IIIIlIllIIlI:IlllllII]          
  elif llllIllIII < lIIIllIlII:
    IlIIIIlIIIlIIIl[IlIIllIlIlIIlIIIllI:lIIIllIlII] = lllIlIlIlllllllll[llllIllIII:lIIIllIlII]          
def IIlIllII(IIllIIIlIIIll):
  lIllIlIIl = len(IIllIIIlIIIll)
  IIlIIIIlIllIIlllIlI = math.ceil(math.log(lIllIlIIl,2))
  lllIlIlIlllllllll, llllllll = IIllIIIlIIIll, [None] * lIllIlIIl               
  for lIllllllIlIllI in (2**lIIlIIlllIIlll for lIIlIIlllIIlll in range(IIlIIIIlIllIIlllIlI)):   
    for lllllIlIII in range(0, lIllIlIIl, 2*lIllllllIlIllI):            
      IlIIIllIl(lllIlIlIlllllllll, llllllll, lllllIlIII, lIllllllIlIllI)
    lllIlIlIlllllllll, llllllll = llllllll, lllIlIlIlllllllll                 
  if IIllIIIlIIIll is not lllIlIlIlllllllll:
    IIllIIIlIIIll[0:lIllIlIIl] = lllIlIlIlllllllll[0:lIllIlIIl]                     