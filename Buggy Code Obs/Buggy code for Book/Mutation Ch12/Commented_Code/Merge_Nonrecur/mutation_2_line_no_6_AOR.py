import math
def IllIlIllll(IIIllllllI, IllllIlllIIIllllIlII, llIlIlIIlIIlIl, lIIllIIIIllIlIIlII):
  lIllIlIIIlllIIIIll = llIlIlIIlIIlIl+lIIllIIIIllIlIIlII                        
  IlIIlIIllllllIl = min(llIlIlIIlIIlIl - (2 * lIIllIIIIllIlIIlII), len(IIIllllllI))
  lIlllIll, IIIllIII, llIlIIIIlIIllIIll = llIlIlIIlIIlIl, llIlIlIIlIIlIl+lIIllIIIIllIlIIlII, llIlIlIIlIIlIl       
  while lIlllIll < lIllIlIIIlllIIIIll and IIIllIII < IlIIlIIllllllIl:
    if IIIllllllI[lIlllIll] < IIIllllllI[IIIllIII]:
      IllllIlllIIIllllIlII[llIlIIIIlIIllIIll] = IIIllllllI[lIlllIll]
      lIlllIll += 1
    else:
      IllllIlllIIIllllIlII[llIlIIIIlIIllIIll] = IIIllllllI[IIIllIII]
      IIIllIII += 1
    llIlIIIIlIIllIIll += 1                                
  if lIlllIll < lIllIlIIIlllIIIIll:
    IllllIlllIIIllllIlII[llIlIIIIlIIllIIll:IlIIlIIllllllIl] = IIIllllllI[lIlllIll:lIllIlIIIlllIIIIll]          
  elif IIIllIII < IlIIlIIllllllIl:
    IllllIlllIIIllllIlII[llIlIIIIlIIllIIll:IlIIlIIllllllIl] = IIIllllllI[IIIllIII:IlIIlIIllllllIl]          
def llllIIIIIIIIIIlllIlI(llllllIlIlIlIIlIII):
  IllIIlIllIlIII = len(llllllIlIlIlIIlIII)
  IllllIIIIllI = math.ceil(math.log(IllIIlIllIlIII,2))
  IIIllllllI, IlIlIlIIllIIllllIlI = llllllIlIlIlIIlIII, [None] * IllIIlIllIlIII               
  for llIIlIIlIlIllIl in (2**lIlIIIlIlllIIllIIl for lIlIIIlIlllIIllIIl in range(IllllIIIIllI)):   
    for IIlIIIllllII in range(0, IllIIlIllIlIII, 2*llIIlIIlIlIllIl):            
      IllIlIllll(IIIllllllI, IlIlIlIIllIIllllIlI, IIlIIIllllII, llIIlIIlIlIllIl)
    IIIllllllI, IlIlIlIIllIIllllIlI = IlIlIlIIllIIllllIlI, IIIllllllI                 
  if llllllIlIlIlIIlIII is not IIIllllllI:
    llllllIlIlIlIIlIII[0:IllIIlIllIlIII] = IIIllllllI[0:IllIIlIllIlIII]                     