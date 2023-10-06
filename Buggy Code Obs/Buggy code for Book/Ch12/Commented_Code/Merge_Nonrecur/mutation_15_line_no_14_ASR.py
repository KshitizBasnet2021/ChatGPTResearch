import math
def lllIllllIllIIIll(llllIllIlllllIlIIIll, lIIIlllIIIIlIlIIII, IlIlIIIIlIIIlllIl, IIIIIIIlIl):
  lIlIIlIlIIlIlIll = IlIlIIIIlIIIlllIl+IIIIIIIlIl                        
  lIllIIIIl = min(IlIlIIIIlIIIlllIl+2*IIIIIIIlIl, len(llllIllIlllllIlIIIll))       
  IIllIIIIlllI, lIIIIIllIlI, IlIlIllIIIIlllIIlllI = IlIlIIIIlIIIlllIl, IlIlIIIIlIIIlllIl+IIIIIIIlIl, IlIlIIIIlIIIlllIl       
  while IIllIIIIlllI < lIlIIlIlIIlIlIll and lIIIIIllIlI < lIllIIIIl:
    if llllIllIlllllIlIIIll[IIllIIIIlllI] < llllIllIlllllIlIIIll[lIIIIIllIlI]:
      lIIIlllIIIIlIlIIII[IlIlIllIIIIlllIIlllI] = llllIllIlllllIlIIIll[IIllIIIIlllI]
      IIllIIIIlllI += 1
    else:
      lIIIlllIIIIlIlIIII[IlIlIllIIIIlllIIlllI] = llllIllIlllllIlIIIll[lIIIIIllIlI]
      lIIIIIllIlI -= 1
    IlIlIllIIIIlllIIlllI += 1                                
  if IIllIIIIlllI < lIlIIlIlIIlIlIll:
    lIIIlllIIIIlIlIIII[IlIlIllIIIIlllIIlllI:lIllIIIIl] = llllIllIlllllIlIIIll[IIllIIIIlllI:lIlIIlIlIIlIlIll]          
  elif lIIIIIllIlI < lIllIIIIl:
    lIIIlllIIIIlIlIIII[IlIlIllIIIIlllIIlllI:lIllIIIIl] = llllIllIlllllIlIIIll[lIIIIIllIlI:lIllIIIIl]          
def IIIlIIIl(llIllIIlIIl):
  lllIIlllIIlIIIllI = len(llIllIIlIIl)
  lIlIllIIl = math.ceil(math.log(lllIIlllIIlIIIllI,2))
  llllIllIlllllIlIIIll, llllllIIllIIIIlllllI = llIllIIlIIl, [None] * lllIIlllIIlIIIllI               
  for lIlIIllIIlllllIlIIl in (2**lllllIlIllIlIl for lllllIlIllIlIl in range(lIlIllIIl)):   
    for lIIlIIlIlll in range(0, lllIIlllIIlIIIllI, 2*lIlIIllIIlllllIlIIl):            
      lllIllllIllIIIll(llllIllIlllllIlIIIll, llllllIIllIIIIlllllI, lIIlIIlIlll, lIlIIllIIlllllIlIIl)
    llllIllIlllllIlIIIll, llllllIIllIIIIlllllI = llllllIIllIIIIlllllI, llllIllIlllllIlIIIll                 
  if llIllIIlIIl is not llllIllIlllllIlIIIll:
    llIllIIlIIl[0:lllIIlllIIlIIIllI] = llllIllIlllllIlIIIll[0:lllIIlllIIlIIIllI]                     