import math
def lIIllIlIIlIIIll(lllIIlllIlIIIllIll, IIIlllIlIlllIIlI, llllllIIl, lIIllIlIIlllllIlll):
  IIIllIlIIllIIII = llllllIIl+lIIllIlIIlllllIlll                        
  lIIIllIlIlIIIIIlIIII = min(llllllIIl+2*lIIllIlIIlllllIlll, len(lllIIlllIlIIIllIll))       
  lIIIlllllIIIlll, lIIIIIIllIlllll, lIllIlIIIlIIIIlI = llllllIIl, llllllIIl+lIIllIlIIlllllIlll, llllllIIl       
  while lIIIlllllIIIlll < IIIllIlIIllIIII and lIIIIIIllIlllll < lIIIllIlIlIIIIIlIIII:
    if lllIIlllIlIIIllIll[lIIIlllllIIIlll] < lllIIlllIlIIIllIll[lIIIIIIllIlllll]:
      IIIlllIlIlllIIlI[lIllIlIIIlIIIIlI] = lllIIlllIlIIIllIll[lIIIlllllIIIlll]
      lIIIlllllIIIlll += 1
    else:
      IIIlllIlIlllIIlI[lIllIlIIIlIIIIlI] = lllIIlllIlIIIllIll[lIIIIIIllIlllll]
      lIIIIIIllIlllll += 1
    lIllIlIIIlIIIIlI += 1                                
  if lIIIlllllIIIlll < IIIllIlIIllIIII:
    IIIlllIlIlllIIlI[lIllIlIIIlIIIIlI:lIIIllIlIlIIIIIlIIII] = lllIIlllIlIIIllIll[lIIIlllllIIIlll:IIIllIlIIllIIII]          
  elif lIIIIIIllIlllll > lIIIllIlIlIIIIIlIIII:
    IIIlllIlIlllIIlI[lIllIlIIIlIIIIlI:lIIIllIlIlIIIIIlIIII] = lllIIlllIlIIIllIll[lIIIIIIllIlllll:lIIIllIlIlIIIIIlIIII]          
def lIIlllllIllI(IlIIIIIlIl):
  lIIIlIlIllIlllII = len(IlIIIIIlIl)
  IIIIIlIII = math.ceil(math.log(lIIIlIlIllIlllII,2))
  lllIIlllIlIIIllIll, llIIIlIIIIIIllIlIII = IlIIIIIlIl, [None] * lIIIlIlIllIlllII               
  for lIIIllll in (2**lIllIlIIllllIlII for lIllIlIIllllIlII in range(IIIIIlIII)):   
    for IlllIlIIIl in range(0, lIIIlIlIllIlllII, 2*lIIIllll):            
      lIIllIlIIlIIIll(lllIIlllIlIIIllIll, llIIIlIIIIIIllIlIII, IlllIlIIIl, lIIIllll)
    lllIIlllIlIIIllIll, llIIIlIIIIIIllIlIII = llIIIlIIIIIIllIlIII, lllIIlllIlIIIllIll                 
  if IlIIIIIlIl is not lllIIlllIlIIIllIll:
    IlIIIIIlIl[0:lIIIlIlIllIlllII] = lllIIlllIlIIIllIll[0:lIIIlIlIllIlllII]                     