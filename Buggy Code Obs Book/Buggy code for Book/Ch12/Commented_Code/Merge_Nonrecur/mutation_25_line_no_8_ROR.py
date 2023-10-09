import math
def IlIIllIIIIlIIlllllI(lllllIIIlllIIIlIll, lllIIlIlIlIll, IIIIIllIllII, lIlIlIllIIIllIIlllI):
  IIlIlllllllI = IIIIIllIllII+lIlIlIllIIIllIIlllI                        
  IllllIlIl = min(IIIIIllIllII+2*lIlIlIllIIIllIIlllI, len(lllllIIIlllIIIlIll))       
  llllllIIIIlII, IIIIIlIIIIllllII, lIlIlIIllIlIIllI = IIIIIllIllII, IIIIIllIllII+lIlIlIllIIIllIIlllI, IIIIIllIllII       
  while (llllllIIIIlII < IIlIlllllllI and IIIIIlIIIIllllII > IllllIlIl):
    if lllllIIIlllIIIlIll[llllllIIIIlII] < lllllIIIlllIIIlIll[IIIIIlIIIIllllII]:
      lllIIlIlIlIll[lIlIlIIllIlIIllI] = lllllIIIlllIIIlIll[llllllIIIIlII]
      llllllIIIIlII += 1
    else:
      lllIIlIlIlIll[lIlIlIIllIlIIllI] = lllllIIIlllIIIlIll[IIIIIlIIIIllllII]
      IIIIIlIIIIllllII += 1
    lIlIlIIllIlIIllI += 1                                
  if llllllIIIIlII < IIlIlllllllI:
    lllIIlIlIlIll[lIlIlIIllIlIIllI:IllllIlIl] = lllllIIIlllIIIlIll[llllllIIIIlII:IIlIlllllllI]          
  elif IIIIIlIIIIllllII < IllllIlIl:
    lllIIlIlIlIll[lIlIlIIllIlIIllI:IllllIlIl] = lllllIIIlllIIIlIll[IIIIIlIIIIllllII:IllllIlIl]          
def IllIllIIlIlllIlIlll(lIlllllllIlI):
  IIIllllIlIlII = len(lIlllllllIlI)
  llIlIIlI = math.ceil(math.log(IIIllllIlIlII,2))
  lllllIIIlllIIIlIll, lIIIlIlIIllIllll = lIlllllllIlI, [None] * IIIllllIlIlII               
  for IIlIIlIII in (2**lIIlllIllIIIlIlllllI for lIIlllIllIIIlIlllllI in range(llIlIIlI)):   
    for lIlIIlIl in range(0, IIIllllIlIlII, 2*IIlIIlIII):            
      IlIIllIIIIlIIlllllI(lllllIIIlllIIIlIll, lIIIlIlIIllIllll, lIlIIlIl, IIlIIlIII)
    lllllIIIlllIIIlIll, lIIIlIlIIllIllll = lIIIlIlIIllIllll, lllllIIIlllIIIlIll                 
  if lIlllllllIlI is not lllllIIIlllIIIlIll:
    lIlllllllIlI[0:IIIllllIlIlII] = lllllIIIlllIIIlIll[0:IIIllllIlIlII]                     