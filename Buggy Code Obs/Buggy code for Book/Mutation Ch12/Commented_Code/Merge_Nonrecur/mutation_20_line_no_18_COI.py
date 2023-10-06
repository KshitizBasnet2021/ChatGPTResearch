import math
def IllIIIllIIlIlIIIll(llIllllIIllll, llIIIlIlIllI, lllIIlIllIIl, IIIIIIIIllllll):
  IlIllllIIIlIIlllIll = lllIIlIllIIl+IIIIIIIIllllll                        
  llIllllIIlllll = min(lllIIlIllIIl+2*IIIIIIIIllllll, len(llIllllIIllll))       
  lIIllllIllI, IIIlllIllIlIllI, lllllIIllIlllll = lllIIlIllIIl, lllIIlIllIIl+IIIIIIIIllllll, lllIIlIllIIl       
  while lIIllllIllI < IlIllllIIIlIIlllIll and IIIlllIllIlIllI < llIllllIIlllll:
    if llIllllIIllll[lIIllllIllI] < llIllllIIllll[IIIlllIllIlIllI]:
      llIIIlIlIllI[lllllIIllIlllll] = llIllllIIllll[lIIllllIllI]
      lIIllllIllI += 1
    else:
      llIIIlIlIllI[lllllIIllIlllll] = llIllllIIllll[IIIlllIllIlIllI]
      IIIlllIllIlIllI += 1
    lllllIIllIlllll += 1                                
  if lIIllllIllI < IlIllllIIIlIIlllIll:
    llIIIlIlIllI[lllllIIllIlllll:llIllllIIlllll] = llIllllIIllll[lIIllllIllI:IlIllllIIIlIIlllIll]          
  elif not (IIIlllIllIlIllI < llIllllIIlllll):
    llIIIlIlIllI[lllllIIllIlllll:llIllllIIlllll] = llIllllIIllll[IIIlllIllIlIllI:llIllllIIlllll]          
def lIlllllllIlllIllIl(IlIlllll):
  IllllIllIlIlIlI = len(IlIlllll)
  lIIIIIlIIlIIlllllI = math.ceil(math.log(IllllIllIlIlIlI,2))
  llIllllIIllll, lIlIlIlIlIlIlIIlIllI = IlIlllll, [None] * IllllIllIlIlIlI               
  for IlllIIlIlIII in (2**IlIllIIllIIllI for IlIllIIllIIllI in range(lIIIIIlIIlIIlllllI)):   
    for llllIllIIIlIlIl in range(0, IllllIllIlIlIlI, 2*IlllIIlIlIII):            
      IllIIIllIIlIlIIIll(llIllllIIllll, lIlIlIlIlIlIlIIlIllI, llllIllIIIlIlIl, IlllIIlIlIII)
    llIllllIIllll, lIlIlIlIlIlIlIIlIllI = lIlIlIlIlIlIlIIlIllI, llIllllIIllll                 
  if IlIlllll is not llIllllIIllll:
    IlIlllll[0:IllllIllIlIlIlI] = llIllllIIllll[0:IllllIllIlIlIlI]                     