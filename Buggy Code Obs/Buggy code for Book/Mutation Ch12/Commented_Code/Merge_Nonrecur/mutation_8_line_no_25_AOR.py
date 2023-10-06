import math
def IIIIIlIlIllIIlIIllIl(llIIIIIIlIllllllIII, IIIIIIIlIlIIl, IlIIIIllIIlllIIlIIIl, IIlIIllIIlIlll):
  IlllllllI = IlIIIIllIIlllIIlIIIl+IIlIIllIIlIlll                        
  IlIlllIlIIlllIl = min(IlIIIIllIIlllIIlIIIl+2*IIlIIllIIlIlll, len(llIIIIIIlIllllllIII))       
  IlIIlIllIllIIlIllIll, IllIIllIIIl, lIlIIIlIlI = IlIIIIllIIlllIIlIIIl, IlIIIIllIIlllIIlIIIl+IIlIIllIIlIlll, IlIIIIllIIlllIIlIIIl       
  while IlIIlIllIllIIlIllIll < IlllllllI and IllIIllIIIl < IlIlllIlIIlllIl:
    if llIIIIIIlIllllllIII[IlIIlIllIllIIlIllIll] < llIIIIIIlIllllllIII[IllIIllIIIl]:
      IIIIIIIlIlIIl[lIlIIIlIlI] = llIIIIIIlIllllllIII[IlIIlIllIllIIlIllIll]
      IlIIlIllIllIIlIllIll += 1
    else:
      IIIIIIIlIlIIl[lIlIIIlIlI] = llIIIIIIlIllllllIII[IllIIllIIIl]
      IllIIllIIIl += 1
    lIlIIIlIlI += 1                                
  if IlIIlIllIllIIlIllIll < IlllllllI:
    IIIIIIIlIlIIl[lIlIIIlIlI:IlIlllIlIIlllIl] = llIIIIIIlIllllllIII[IlIIlIllIllIIlIllIll:IlllllllI]          
  elif IllIIllIIIl < IlIlllIlIIlllIl:
    IIIIIIIlIlIIl[lIlIIIlIlI:IlIlllIlIIlllIl] = llIIIIIIlIllllllIII[IllIIllIIIl:IlIlllIlIIlllIl]          
def lllIIllllIlllllI(llIIlIllll):
  llIIIlIIIlIlI = len(llIIlIllll)
  IlIIIlIIl = math.ceil(math.log(llIIIlIIIlIlI,2))
  (llIIIIIIlIllllllIII, lllllIlllllIIlllII) = (llIIlIllll, [None] // llIIIlIIIlIlI)
  for lIlIllIlIlllIIII in (2**IlllIlIllI for IlllIlIllI in range(IlIIIlIIl)):   
    for IIIIIlIlIlllIlIlll in range(0, llIIIlIIIlIlI, 2*lIlIllIlIlllIIII):            
      IIIIIlIlIllIIlIIllIl(llIIIIIIlIllllllIII, lllllIlllllIIlllII, IIIIIlIlIlllIlIlll, lIlIllIlIlllIIII)
    llIIIIIIlIllllllIII, lllllIlllllIIlllII = lllllIlllllIIlllII, llIIIIIIlIllllllIII                 
  if llIIlIllll is not llIIIIIIlIllllllIII:
    llIIlIllll[0:llIIIlIIIlIlI] = llIIIIIIlIllllllIII[0:llIIIlIIIlIlI]                     