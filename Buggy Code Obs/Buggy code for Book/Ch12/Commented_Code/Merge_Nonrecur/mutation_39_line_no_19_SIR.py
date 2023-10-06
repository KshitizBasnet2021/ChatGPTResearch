import math
def IllIIIlIIIlllllI(IlIllIIl, IlIIIIIlIl, IIlIIlIIIlllIllll, lIIlIllIIlIIIIl):
  IllllllIIIIIIIIllI = IIlIIlIIIlllIllll+lIIlIllIIlIIIIl                        
  lIlIlllllllIllllIIl = min(IIlIIlIIIlllIllll+2*lIIlIllIIlIIIIl, len(IlIllIIl))       
  lllllIIIllIIIIIlI, IIlIIllIIlIIIl, IIIIlIIlIIIl = IIlIIlIIIlllIllll, IIlIIlIIIlllIllll+lIIlIllIIlIIIIl, IIlIIlIIIlllIllll       
  while lllllIIIllIIIIIlI < IllllllIIIIIIIIllI and IIlIIllIIlIIIl < lIlIlllllllIllllIIl:
    if IlIllIIl[lllllIIIllIIIIIlI] < IlIllIIl[IIlIIllIIlIIIl]:
      IlIIIIIlIl[IIIIlIIlIIIl] = IlIllIIl[lllllIIIllIIIIIlI]
      lllllIIIllIIIIIlI += 1
    else:
      IlIIIIIlIl[IIIIlIIlIIIl] = IlIllIIl[IIlIIllIIlIIIl]
      IIlIIllIIlIIIl += 1
    IIIIlIIlIIIl += 1                                
  if lllllIIIllIIIIIlI < IllllllIIIIIIIIllI:
    IlIIIIIlIl[IIIIlIIlIIIl:lIlIlllllllIllllIIl] = IlIllIIl[lllllIIIllIIIIIlI:IllllllIIIIIIIIllI]          
  elif IIlIIllIIlIIIl < lIlIlllllllIllllIIl:
    IlIIIIIlIl[IIIIlIIlIIIl:lIlIlllllllIllllIIl] = IlIllIIl[:lIlIlllllllIllllIIl]
def IIIlllIlIIlIIl(lIIIllIIl):
  IllllIlIlII = len(lIIIllIIl)
  llIIIIIIIIll = math.ceil(math.log(IllllIlIlII,2))
  IlIllIIl, lIIIIllIIlllIIIllll = lIIIllIIl, [None] * IllllIlIlII               
  for lIllllIIIllllIIl in (2**lIlIlIIlIlIIIl for lIlIlIIlIlIIIl in range(llIIIIIIIIll)):   
    for llIIIlIlIl in range(0, IllllIlIlII, 2*lIllllIIIllllIIl):            
      IllIIIlIIIlllllI(IlIllIIl, lIIIIllIIlllIIIllll, llIIIlIlIl, lIllllIIIllllIIl)
    IlIllIIl, lIIIIllIIlllIIIllll = lIIIIllIIlllIIIllll, IlIllIIl                 
  if lIIIllIIl is not IlIllIIl:
    lIIIllIIl[0:IllllIlIlII] = IlIllIIl[0:IllllIlIlII]                     