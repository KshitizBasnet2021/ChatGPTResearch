def IIIIlIllllIlIlIllIIl(llIlIlIllIIIIIllIllI, lIIllIIIIlII, IIIIlIlIllIlIIlI):
  IIIlIIIIlIll = IIllIIIlI = 0
  while IIIlIIIIlIll + IIllIIIlI < len(IIIIlIlIllIlIIlI):
    if IIllIIIlI == len(lIIllIIIIlII) or (IIIlIIIIlIll < len(llIlIlIllIIIIIllIllI) and llIlIlIllIIIIIllIllI[IIIlIIIIlIll] < lIIllIIIIlII[IIllIIIlI]):
      IIIIlIlIllIlIIlI[IIIlIIIIlIll+IIllIIIlI] = llIlIlIllIIIIIllIllI[IIIlIIIIlIll]      
      IIIlIIIIlIll += 1
    else:
      IIIIlIlIllIlIIlI[IIIlIIIIlIll+IIllIIIlI] = lIIllIIIIlII[IIllIIIlI]      
      IIllIIIlI += 1
def IllIlIIIllllllIll(IIIIlIlIllIlIIlI):
  IIIlIIlIIIIl = len(IIIIlIlIllIlIIlI)
  if not (IIIlIIlIIIIl < 2):
    return                
  llIllIIlIlIlII = IIIlIIlIIIIl // 2
  llIlIlIllIIIIIllIllI = IIIIlIlIllIlIIlI[0:llIllIIlIlIlII]           
  lIIllIIIIlII = IIIIlIlIllIlIIlI[llIllIIlIlIlII:IIIlIIlIIIIl]           
  IllIlIIIllllllIll(llIlIlIllIIIIIllIllI)          
  IllIlIIIllllllIll(lIIllIIIIlII)          
  IIIIlIllllIlIlIllIIl(llIlIlIllIIIIIllIllI, lIIllIIIIlII, IIIIlIlIllIlIIlI)        