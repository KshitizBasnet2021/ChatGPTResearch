import math
def lIIlIIIIlll(IlIIlIIlIIllIIl, lIIIIIIll, IIIlIIIIII, lllIlIIIl):
  lIlllIIllIIIlIlIll = IIIlIIIIII+lllIlIIIl                        
  lIlllIllIIllllIlIII = min(IIIlIIIIII+2*lllIlIIIl, len(IlIIlIIlIIllIIl))       
  IIllIIlIllIllII, IllllIllIlIIIl, llIlIIIIllIIl = IIIlIIIIII, IIIlIIIIII+lllIlIIIl, IIIlIIIIII       
  while IIllIIlIllIllII < lIlllIIllIIIlIlIll and IllllIllIlIIIl < lIlllIllIIllllIlIII:
    if IlIIlIIlIIllIIl[IIllIIlIllIllII] < IlIIlIIlIIllIIl[IllllIllIlIIIl]:
      lIIIIIIll[llIlIIIIllIIl] = IlIIlIIlIIllIIl[IIllIIlIllIllII]
      IIllIIlIllIllII += 1
    else:
      lIIIIIIll[llIlIIIIllIIl] = IlIIlIIlIIllIIl[IllllIllIlIIIl]
      IllllIllIlIIIl += 1
    llIlIIIIllIIl += 1                                
  if IIllIIlIllIllII < lIlllIIllIIIlIlIll:
    lIIIIIIll[llIlIIIIllIIl:lIlllIllIIllllIlIII] = IlIIlIIlIIllIIl[IIllIIlIllIllII:lIlllIIllIIIlIlIll]          
  elif IllllIllIlIIIl < lIlllIllIIllllIlIII:
    lIIIIIIll[llIlIIIIllIIl:lIlllIllIIllllIlIII] = IlIIlIIlIIllIIl[IllllIllIlIIIl:lIlllIllIIllllIlIII]          
def IlIIIIllI(IIlIlIlIIIII):
  IIlIllIllIIlI = len(IIlIlIlIIIII)
  IllllIIlIlIII = math.ceil(math.log(IIlIllIllIIlI,2))
  IlIIlIIlIIllIIl, IIllllIlIll = IIlIlIlIIIII, [None] * IIlIllIllIIlI               
  for IlIlIlIllllllllIlI in (2**lIlIllIIIIllIIIlII for lIlIllIIIIllIIIlII in range(IllllIIlIlIII)):   
    for lIIIIIIllIIlll in range(0, IIlIllIllIIlI, 2*IlIlIlIllllllllIlI):            
      lIIlIIIIlll(IlIIlIIlIIllIIl, IIllllIlIll, lIIIIIIllIIlll, IlIlIlIllllllllIlI)
    IlIIlIIlIIllIIl, IIllllIlIll = IIllllIlIll, IlIIlIIlIIllIIl                 
  if IIlIlIlIIIII is not IlIIlIIlIIllIIl:
    IIlIlIlIIIII[:IIlIllIllIIlI] = IlIIlIIlIIllIIl[0:IIlIllIllIIlI]