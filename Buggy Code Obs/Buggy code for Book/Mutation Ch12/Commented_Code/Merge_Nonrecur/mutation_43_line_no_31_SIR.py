import math
def lllIIllIllllI(IIIlllllIl, lllllIlllllll, IIlllllllIl, IIlIIlllIIl):
  lIllllllIllIlIlllIl = IIlllllllIl+IIlIIlllIIl                        
  IIIIIllIlIIIIlI = min(IIlllllllIl+2*IIlIIlllIIl, len(IIIlllllIl))       
  lIIIIlIlIl, lIllIlII, lIIlIlllIlllIlIlll = IIlllllllIl, IIlllllllIl+IIlIIlllIIl, IIlllllllIl       
  while lIIIIlIlIl < lIllllllIllIlIlllIl and lIllIlII < IIIIIllIlIIIIlI:
    if IIIlllllIl[lIIIIlIlIl] < IIIlllllIl[lIllIlII]:
      lllllIlllllll[lIIlIlllIlllIlIlll] = IIIlllllIl[lIIIIlIlIl]
      lIIIIlIlIl += 1
    else:
      lllllIlllllll[lIIlIlllIlllIlIlll] = IIIlllllIl[lIllIlII]
      lIllIlII += 1
    lIIlIlllIlllIlIlll += 1                                
  if lIIIIlIlIl < lIllllllIllIlIlllIl:
    lllllIlllllll[lIIlIlllIlllIlIlll:IIIIIllIlIIIIlI] = IIIlllllIl[lIIIIlIlIl:lIllllllIllIlIlllIl]          
  elif lIllIlII < IIIIIllIlIIIIlI:
    lllllIlllllll[lIIlIlllIlllIlIlll:IIIIIllIlIIIIlI] = IIIlllllIl[lIllIlII:IIIIIllIlIIIIlI]          
def IlIIlllIllllllIIlIIl(llIIIIllllIIIlllI):
  lIIlIllIIlIlllIl = len(llIIIIllllIIIlllI)
  IlIlIIIIlI = math.ceil(math.log(lIIlIllIIlIlllIl,2))
  IIIlllllIl, IlIlIIllIIll = llIIIIllllIIIlllI, [None] * lIIlIllIIlIlllIl               
  for IlIIIlllIIIII in (2**llIlIIIllIIIllIIIl for llIlIIIllIIIllIIIl in range(IlIlIIIIlI)):   
    for lIlIlllIIlllIIIl in range(0, lIIlIllIIlIlllIl, 2*IlIIIlllIIIII):            
      lllIIllIllllI(IIIlllllIl, IlIlIIllIIll, lIlIlllIIlllIIIl, IlIIIlllIIIII)
    IIIlllllIl, IlIlIIllIIll = IlIlIIllIIll, IIIlllllIl                 
  if llIIIIllllIIIlllI is not IIIlllllIl:
    llIIIIllllIIIlllI[0:lIIlIllIIlIlllIl] = IIIlllllIl[:lIIlIllIIlIlllIl]