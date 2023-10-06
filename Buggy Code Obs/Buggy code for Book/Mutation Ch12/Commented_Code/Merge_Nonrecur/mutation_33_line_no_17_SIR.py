import math
def lIIIllIIIIl(IIIIIlIlIIlIlI, IIlIlIllIlIIIllI, lIIIllIIIllIIllIII, IlIllIllllllIlI):
  lIllllIIIllIlll = lIIIllIIIllIIllIII+IlIllIllllllIlI                        
  IlIIIIIlllIlllllIII = min(lIIIllIIIllIIllIII+2*IlIllIllllllIlI, len(IIIIIlIlIIlIlI))       
  llIlIIll, IlIlIlIllIll, lIIlIIlIlllI = lIIIllIIIllIIllIII, lIIIllIIIllIIllIII+IlIllIllllllIlI, lIIIllIIIllIIllIII       
  while llIlIIll < lIllllIIIllIlll and IlIlIlIllIll < IlIIIIIlllIlllllIII:
    if IIIIIlIlIIlIlI[llIlIIll] < IIIIIlIlIIlIlI[IlIlIlIllIll]:
      IIlIlIllIlIIIllI[lIIlIIlIlllI] = IIIIIlIlIIlIlI[llIlIIll]
      llIlIIll += 1
    else:
      IIlIlIllIlIIIllI[lIIlIIlIlllI] = IIIIIlIlIIlIlI[IlIlIlIllIll]
      IlIlIlIllIll += 1
    lIIlIIlIlllI += 1                                
  if llIlIIll < lIllllIIIllIlll:
    IIlIlIllIlIIIllI[:IlIIIIIlllIlllllIII] = IIIIIlIlIIlIlI[llIlIIll:lIllllIIIllIlll]
  elif IlIlIlIllIll < IlIIIIIlllIlllllIII:
    IIlIlIllIlIIIllI[lIIlIIlIlllI:IlIIIIIlllIlllllIII] = IIIIIlIlIIlIlI[IlIlIlIllIll:IlIIIIIlllIlllllIII]          
def IIIIlIlIIlIlIlllIllI(lllIIlllIlII):
  lIllllIIlIIIllIlI = len(lllIIlllIlII)
  llIlIlllIIIIllIlII = math.ceil(math.log(lIllllIIlIIIllIlI,2))
  IIIIIlIlIIlIlI, lIlllIIll = lllIIlllIlII, [None] * lIllllIIlIIIllIlI               
  for lIIIllllIIlllIIIlll in (2**IlIllIIIIIlIlIl for IlIllIIIIIlIlIl in range(llIlIlllIIIIllIlII)):   
    for lIIIlIlIlIll in range(0, lIllllIIlIIIllIlI, 2*lIIIllllIIlllIIIlll):            
      lIIIllIIIIl(IIIIIlIlIIlIlI, lIlllIIll, lIIIlIlIlIll, lIIIllllIIlllIIIlll)
    IIIIIlIlIIlIlI, lIlllIIll = lIlllIIll, IIIIIlIlIIlIlI                 
  if lllIIlllIlII is not IIIIIlIlIIlIlI:
    lllIIlllIlII[0:lIllllIIlIIIllIlI] = IIIIIlIlIIlIlI[0:lIllllIIlIIIllIlI]                     