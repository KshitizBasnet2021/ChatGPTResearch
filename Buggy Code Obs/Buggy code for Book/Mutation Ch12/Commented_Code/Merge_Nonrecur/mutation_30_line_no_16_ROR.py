import math
def lIIIllIIIIlllIlIIl(lllllIlIllllIllllI, lIlllllIII, llIIIlllIlll, IllIllIIll):
  lllllllII = llIIIlllIlll+IllIllIIll                        
  llIllIIIIIlI = min(llIIIlllIlll+2*IllIllIIll, len(lllllIlIllllIllllI))       
  llIllllIlllIll, IIIIIIlIIlIllI, IIlIlllIllIIllIlIIl = llIIIlllIlll, llIIIlllIlll+IllIllIIll, llIIIlllIlll       
  while llIllllIlllIll < lllllllII and IIIIIIlIIlIllI < llIllIIIIIlI:
    if lllllIlIllllIllllI[llIllllIlllIll] < lllllIlIllllIllllI[IIIIIIlIIlIllI]:
      lIlllllIII[IIlIlllIllIIllIlIIl] = lllllIlIllllIllllI[llIllllIlllIll]
      llIllllIlllIll += 1
    else:
      lIlllllIII[IIlIlllIllIIllIlIIl] = lllllIlIllllIllllI[IIIIIIlIIlIllI]
      IIIIIIlIIlIllI += 1
    IIlIlllIllIIllIlIIl += 1                                
  if llIllllIlllIll <= lllllllII:
    lIlllllIII[IIlIlllIllIIllIlIIl:llIllIIIIIlI] = lllllIlIllllIllllI[llIllllIlllIll:lllllllII]          
  elif IIIIIIlIIlIllI < llIllIIIIIlI:
    lIlllllIII[IIlIlllIllIIllIlIIl:llIllIIIIIlI] = lllllIlIllllIllllI[IIIIIIlIIlIllI:llIllIIIIIlI]          
def IIIIIIlIIIlIlI(lllIllIIIIIllll):
  llllIlIIlIII = len(lllIllIIIIIllll)
  IlIIIlllIlIIIIIl = math.ceil(math.log(llllIlIIlIII,2))
  lllllIlIllllIllllI, IIlIIlIllIIIllllIl = lllIllIIIIIllll, [None] * llllIlIIlIII               
  for IlIlllllIlIII in (2**lllIlllIlIlIlI for lllIlllIlIlIlI in range(IlIIIlllIlIIIIIl)):   
    for lIIllIlll in range(0, llllIlIIlIII, 2*IlIlllllIlIII):            
      lIIIllIIIIlllIlIIl(lllllIlIllllIllllI, IIlIIlIllIIIllllIl, lIIllIlll, IlIlllllIlIII)
    lllllIlIllllIllllI, IIlIIlIllIIIllllIl = IIlIIlIllIIIllllIl, lllllIlIllllIllllI                 
  if lllIllIIIIIllll is not lllllIlIllllIllllI:
    lllIllIIIIIllll[0:llllIlIIlIII] = lllllIlIllllIllllI[0:llllIlIIlIII]                     