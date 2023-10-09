import math
def llIIllllIII(lIllIIllIlllIlIIIlll, llIIlIlllIIIIll, IIIlllIlIll, IlIllIIlllllIl):
  lllIIlIIIIllIlIllII = IIIlllIlIll+IlIllIIlllllIl                        
  lllIIlIIllIlIIlIl = min(IIIlllIlIll+2*IlIllIIlllllIl, len(lIllIIllIlllIlIIIlll))       
  lIlIllIII, lIlllIIII, lllIIIIIlIII = IIIlllIlIll, IIIlllIlIll+IlIllIIlllllIl, IIIlllIlIll       
  while (lIlIllIII <= lllIIlIIIIllIlIllII and lIlllIIII < lllIIlIIllIlIIlIl):
    if lIllIIllIlllIlIIIlll[lIlIllIII] < lIllIIllIlllIlIIIlll[lIlllIIII]:
      llIIlIlllIIIIll[lllIIIIIlIII] = lIllIIllIlllIlIIIlll[lIlIllIII]
      lIlIllIII += 1
    else:
      llIIlIlllIIIIll[lllIIIIIlIII] = lIllIIllIlllIlIIIlll[lIlllIIII]
      lIlllIIII += 1
    lllIIIIIlIII += 1                                
  if lIlIllIII < lllIIlIIIIllIlIllII:
    llIIlIlllIIIIll[lllIIIIIlIII:lllIIlIIllIlIIlIl] = lIllIIllIlllIlIIIlll[lIlIllIII:lllIIlIIIIllIlIllII]          
  elif lIlllIIII < lllIIlIIllIlIIlIl:
    llIIlIlllIIIIll[lllIIIIIlIII:lllIIlIIllIlIIlIl] = lIllIIllIlllIlIIIlll[lIlllIIII:lllIIlIIllIlIIlIl]          
def IlIIIIIIlIlIlIlIlII(IlIlllIIlIlllIlll):
  lllIIIIlllIlI = len(IlIlllIIlIlllIlll)
  llllllIllIIIllIl = math.ceil(math.log(lllIIIIlllIlI,2))
  lIllIIllIlllIlIIIlll, llIIIIllIlIIlIlIIIlI = IlIlllIIlIlllIlll, [None] * lllIIIIlllIlI               
  for IlIIIllIIIl in (2**lllIllIl for lllIllIl in range(llllllIllIIIllIl)):   
    for IlIIIIllIIlIIlIIlIIl in range(0, lllIIIIlllIlI, 2*IlIIIllIIIl):            
      llIIllllIII(lIllIIllIlllIlIIIlll, llIIIIllIlIIlIlIIIlI, IlIIIIllIIlIIlIIlIIl, IlIIIllIIIl)
    lIllIIllIlllIlIIIlll, llIIIIllIlIIlIlIIIlI = llIIIIllIlIIlIlIIIlI, lIllIIllIlllIlIIIlll                 
  if IlIlllIIlIlllIlll is not lIllIIllIlllIlIIIlll:
    IlIlllIIlIlllIlll[0:lllIIIIlllIlI] = lIllIIllIlllIlIIIlll[0:lllIIIIlllIlI]                     