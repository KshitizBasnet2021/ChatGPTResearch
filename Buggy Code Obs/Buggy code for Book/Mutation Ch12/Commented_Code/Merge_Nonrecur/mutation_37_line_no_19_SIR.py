import math
def IlllIlIIIIIlIl(IIlIIllIIlllIIIIll, IIIlllIIIIIllI, lIlIllIlI, IIllIIlIIllI):
  IIIlIllIlIllIIlllIl = lIlIllIlI+IIllIIlIIllI                        
  IllIlIlII = min(lIlIllIlI+2*IIllIIlIIllI, len(IIlIIllIIlllIIIIll))       
  IIIllllllIlll, lllIIIIII, IllllIIl = lIlIllIlI, lIlIllIlI+IIllIIlIIllI, lIlIllIlI       
  while IIIllllllIlll < IIIlIllIlIllIIlllIl and lllIIIIII < IllIlIlII:
    if IIlIIllIIlllIIIIll[IIIllllllIlll] < IIlIIllIIlllIIIIll[lllIIIIII]:
      IIIlllIIIIIllI[IllllIIl] = IIlIIllIIlllIIIIll[IIIllllllIlll]
      IIIllllllIlll += 1
    else:
      IIIlllIIIIIllI[IllllIIl] = IIlIIllIIlllIIIIll[lllIIIIII]
      lllIIIIII += 1
    IllllIIl += 1                                
  if IIIllllllIlll < IIIlIllIlIllIIlllIl:
    IIIlllIIIIIllI[IllllIIl:IllIlIlII] = IIlIIllIIlllIIIIll[IIIllllllIlll:IIIlIllIlIllIIlllIl]          
  elif lllIIIIII < IllIlIlII:
    IIIlllIIIIIllI[:IllIlIlII] = IIlIIllIIlllIIIIll[lllIIIIII:IllIlIlII]
def llIllllIlllIIllI(llllIIlllIlllllIl):
  lllIIIlIIlIlllIIIIIl = len(llllIIlllIlllllIl)
  IlllIIlIIllIllllll = math.ceil(math.log(lllIIIlIIlIlllIIIIIl,2))
  IIlIIllIIlllIIIIll, IllllllIllIllI = llllIIlllIlllllIl, [None] * lllIIIlIIlIlllIIIIIl               
  for IllllIIIIIIII in (2**lIIIlIIIllIII for lIIIlIIIllIII in range(IlllIIlIIllIllllll)):   
    for IlIlIlllllllllllllIl in range(0, lllIIIlIIlIlllIIIIIl, 2*IllllIIIIIIII):            
      IlllIlIIIIIlIl(IIlIIllIIlllIIIIll, IllllllIllIllI, IlIlIlllllllllllllIl, IllllIIIIIIII)
    IIlIIllIIlllIIIIll, IllllllIllIllI = IllllllIllIllI, IIlIIllIIlllIIIIll                 
  if llllIIlllIlllllIl is not IIlIIllIIlllIIIIll:
    llllIIlllIlllllIl[0:lllIIIlIIlIlllIIIIIl] = IIlIIllIIlllIIIIll[0:lllIIIlIIlIlllIIIIIl]                     