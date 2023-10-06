import math
def lIlIllIllIlIIlIlll(IllIIIlIlIllIl, IIIlIllIlIllII, lIIlllIlI, llIIlllI):
  IlIlIlIlI = lIIlllIlI+llIIlllI                        
  lIlIlIlIlIIIlIlI = min(lIIlllIlI+2*llIIlllI, len(IllIIIlIlIllIl))       
  lIlllIllllII, IIIllIIll, IlIllIIIllIIIIIllll = lIIlllIlI, lIIlllIlI+llIIlllI, lIIlllIlI       
  while lIlllIllllII < IlIlIlIlI and IIIllIIll < lIlIlIlIlIIIlIlI:
    if IllIIIlIlIllIl[lIlllIllllII] < IllIIIlIlIllIl[IIIllIIll]:
      IIIlIllIlIllII[IlIllIIIllIIIIIllll] = IllIIIlIlIllIl[lIlllIllllII]
      lIlllIllllII += 1
    else:
      IIIlIllIlIllII[IlIllIIIllIIIIIllll] = IllIIIlIlIllIl[IIIllIIll]
      IIIllIIll += 1
    IlIllIIIllIIIIIllll -= 1
  if lIlllIllllII < IlIlIlIlI:
    IIIlIllIlIllII[IlIllIIIllIIIIIllll:lIlIlIlIlIIIlIlI] = IllIIIlIlIllIl[lIlllIllllII:IlIlIlIlI]          
  elif IIIllIIll < lIlIlIlIlIIIlIlI:
    IIIlIllIlIllII[IlIllIIIllIIIIIllll:lIlIlIlIlIIIlIlI] = IllIIIlIlIllIl[IIIllIIll:lIlIlIlIlIIIlIlI]          
def lIllIIIl(lIIlllIlII):
  lIIIllIllIIl = len(lIIlllIlII)
  llIIIllIIlII = math.ceil(math.log(lIIIllIllIIl,2))
  IllIIIlIlIllIl, IIlIIIllllIlIlI = lIIlllIlII, [None] * lIIIllIllIIl               
  for lIIllIlIllllIII in (2**lIIIlIIllII for lIIIlIIllII in range(llIIIllIIlII)):   
    for lllIlllIlIIl in range(0, lIIIllIllIIl, 2*lIIllIlIllllIII):            
      lIlIllIllIlIIlIlll(IllIIIlIlIllIl, IIlIIIllllIlIlI, lllIlllIlIIl, lIIllIlIllllIII)
    IllIIIlIlIllIl, IIlIIIllllIlIlI = IIlIIIllllIlIlI, IllIIIlIlIllIl                 
  if lIIlllIlII is not IllIIIlIlIllIl:
    lIIlllIlII[0:lIIIllIllIIl] = IllIIIlIlIllIl[0:lIIIllIllIIl]                     