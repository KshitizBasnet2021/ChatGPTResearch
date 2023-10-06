import math
def IlllllllllllIII(lllIlIIl, IlIllIlIlIl, llIIlIIllIlIIIII, lIlllllllIllIllIllIl):
  IIIIlIlI = llIIlIIllIlIIIII+lIlllllllIllIllIllIl                        
  IlllIIllIIl = min(llIIlIIllIlIIIII+2*lIlllllllIllIllIllIl, len(lllIlIIl))       
  lIIIlllllIIllIl, lIIIIIlIlIIlI, llllllIllIl = llIIlIIllIlIIIII, llIIlIIllIlIIIII+lIlllllllIllIllIllIl, llIIlIIllIlIIIII       
  while (lIIIlllllIIllIl > IIIIlIlI and lIIIIIlIlIIlI < IlllIIllIIl):
    if lllIlIIl[lIIIlllllIIllIl] < lllIlIIl[lIIIIIlIlIIlI]:
      IlIllIlIlIl[llllllIllIl] = lllIlIIl[lIIIlllllIIllIl]
      lIIIlllllIIllIl += 1
    else:
      IlIllIlIlIl[llllllIllIl] = lllIlIIl[lIIIIIlIlIIlI]
      lIIIIIlIlIIlI += 1
    llllllIllIl += 1                                
  if lIIIlllllIIllIl < IIIIlIlI:
    IlIllIlIlIl[llllllIllIl:IlllIIllIIl] = lllIlIIl[lIIIlllllIIllIl:IIIIlIlI]          
  elif lIIIIIlIlIIlI < IlllIIllIIl:
    IlIllIlIlIl[llllllIllIl:IlllIIllIIl] = lllIlIIl[lIIIIIlIlIIlI:IlllIIllIIl]          
def IIIIIllIllIlllIII(llIIIllIIll):
  lIIIlllIlI = len(llIIIllIIll)
  lIIlIIlllIIIIIIlIIll = math.ceil(math.log(lIIIlllIlI,2))
  lllIlIIl, llIlIIlII = llIIIllIIll, [None] * lIIIlllIlI               
  for IIlIIIIll in (2**llllIIIIlIIIIIIllIIl for llllIIIIlIIIIIIllIIl in range(lIIlIIlllIIIIIIlIIll)):   
    for llIIIlllIlllIlllIll in range(0, lIIIlllIlI, 2*IIlIIIIll):            
      IlllllllllllIII(lllIlIIl, llIlIIlII, llIIIlllIlllIlllIll, IIlIIIIll)
    lllIlIIl, llIlIIlII = llIlIIlII, lllIlIIl                 
  if llIIIllIIll is not lllIlIIl:
    llIIIllIIll[0:lIIIlllIlI] = lllIlIIl[0:lIIIlllIlI]                     