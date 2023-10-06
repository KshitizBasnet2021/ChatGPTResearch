import math
def IlIlIIlIlllIlll(lIIlIIIlIIIIlIIl, llIlIlIIllIII, IlllIIlIlllllIll, IlIllIIlIlIllllIIIlI):
  lIIlIIIlIlIII = IlllIIlIlllllIll+IlIllIIlIlIllllIIIlI                        
  IIlIIIlIlI = min(IlllIIlIlllllIll+2*IlIllIIlIlIllllIIIlI, len(lIIlIIIlIIIIlIIl))       
  llIlIIlllllllIIlllll, lIIlIIIIIIlIllI, IIIlllIIIlIllIII = IlllIIlIlllllIll, IlllIIlIlllllIll+IlIllIIlIlIllllIIIlI, IlllIIlIlllllIll       
  while llIlIIlllllllIIlllll < lIIlIIIlIlIII and lIIlIIIIIIlIllI < IIlIIIlIlI:
    if lIIlIIIlIIIIlIIl[llIlIIlllllllIIlllll] < lIIlIIIlIIIIlIIl[lIIlIIIIIIlIllI]:
      llIlIlIIllIII[IIIlllIIIlIllIII] = lIIlIIIlIIIIlIIl[llIlIIlllllllIIlllll]
      llIlIIlllllllIIlllll += 1
    else:
      llIlIlIIllIII[IIIlllIIIlIllIII] = lIIlIIIlIIIIlIIl[lIIlIIIIIIlIllI]
      lIIlIIIIIIlIllI += 1
    IIIlllIIIlIllIII += 1                                
  if llIlIIlllllllIIlllll < lIIlIIIlIlIII:
    llIlIlIIllIII[IIIlllIIIlIllIII:IIlIIIlIlI] = lIIlIIIlIIIIlIIl[llIlIIlllllllIIlllll:lIIlIIIlIlIII]          
  elif lIIlIIIIIIlIllI < IIlIIIlIlI:
    llIlIlIIllIII[IIIlllIIIlIllIII:IIlIIIlIlI] = lIIlIIIlIIIIlIIl[lIIlIIIIIIlIllI:IIlIIIlIlI]          
def llllIllIlllllIlllI(lIIlIllIlIllll):
  lIIllllIIIIIll = len(lIIlIllIlIllll)
  lIIIllIlIl = math.ceil(math.log(lIIllllIIIIIll,2))
  lIIlIIIlIIIIlIIl, lIlIIIlIIlllIllIIIIl = lIIlIllIlIllll, [None] * lIIllllIIIIIll               
  for IlIlIIIIlIIlIllIlIl in (2**lIlIIlllIlII for lIlIIlllIlII in range(lIIIllIlIl)):   
    for IIlIlIllI in range(0, lIIllllIIIIIll, 2*IlIlIIIIlIIlIllIlIl):            
      IlIlIIlIlllIlll(lIIlIIIlIIIIlIIl, lIlIIIlIIlllIllIIIIl, IIlIlIllI, IlIlIIIIlIIlIllIlIl)
    lIIlIIIlIIIIlIIl, lIlIIIlIIlllIllIIIIl = lIlIIIlIIlllIllIIIIl, lIIlIIIlIIIIlIIl                 
  if lIIlIllIlIllll is not lIIlIIIlIIIIlIIl:
    lIIlIllIlIllll[0:] = lIIlIIIlIIIIlIIl[0:lIIllllIIIIIll]