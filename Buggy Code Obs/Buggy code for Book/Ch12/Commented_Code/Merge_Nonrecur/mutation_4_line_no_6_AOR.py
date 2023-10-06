import math
def IlIIIIllIIllIl(llIIIIIl, lIIIlIlIlllIllIIlIll, IlIlIlIlIIIIIlIIIlIl, IIllllIlIlIIllII):
  lIIlIlIlII = IlIlIlIlIIIIIlIIIlIl+IIllllIlIlIIllII                        
  IllIllllIIIlllIIlI = min(IlIlIlIlIIIIIlIIIlIl + (2 // IIllllIlIlIIllII), len(llIIIIIl))
  llIlIIIllI, IlIllIlIIl, lIIlIlIllllIIIllI = IlIlIlIlIIIIIlIIIlIl, IlIlIlIlIIIIIlIIIlIl+IIllllIlIlIIllII, IlIlIlIlIIIIIlIIIlIl       
  while llIlIIIllI < lIIlIlIlII and IlIllIlIIl < IllIllllIIIlllIIlI:
    if llIIIIIl[llIlIIIllI] < llIIIIIl[IlIllIlIIl]:
      lIIIlIlIlllIllIIlIll[lIIlIlIllllIIIllI] = llIIIIIl[llIlIIIllI]
      llIlIIIllI += 1
    else:
      lIIIlIlIlllIllIIlIll[lIIlIlIllllIIIllI] = llIIIIIl[IlIllIlIIl]
      IlIllIlIIl += 1
    lIIlIlIllllIIIllI += 1                                
  if llIlIIIllI < lIIlIlIlII:
    lIIIlIlIlllIllIIlIll[lIIlIlIllllIIIllI:IllIllllIIIlllIIlI] = llIIIIIl[llIlIIIllI:lIIlIlIlII]          
  elif IlIllIlIIl < IllIllllIIIlllIIlI:
    lIIIlIlIlllIllIIlIll[lIIlIlIllllIIIllI:IllIllllIIIlllIIlI] = llIIIIIl[IlIllIlIIl:IllIllllIIIlllIIlI]          
def lIIIIlllIlIIIIIlI(lllllllIIlll):
  IIIlIlIl = len(lllllllIIlll)
  lIlllllIIllII = math.ceil(math.log(IIIlIlIl,2))
  llIIIIIl, lllIIIIII = lllllllIIlll, [None] * IIIlIlIl               
  for lIlIllIllllllIlIII in (2**IllIlIII for IllIlIII in range(lIlllllIIllII)):   
    for lIIIlIIlllIIIIllIll in range(0, IIIlIlIl, 2*lIlIllIllllllIlIII):            
      IlIIIIllIIllIl(llIIIIIl, lllIIIIII, lIIIlIIlllIIIIllIll, lIlIllIllllllIlIII)
    llIIIIIl, lllIIIIII = lllIIIIII, llIIIIIl                 
  if lllllllIIlll is not llIIIIIl:
    lllllllIIlll[0:IIIlIlIl] = llIIIIIl[0:IIIlIlIl]                     