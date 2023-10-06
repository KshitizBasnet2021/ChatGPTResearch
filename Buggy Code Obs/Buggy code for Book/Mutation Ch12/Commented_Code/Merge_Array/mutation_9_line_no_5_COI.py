def IIIlIIIIIIIlIlIl(IIlllIllIIllIl, IIlIIIlIlIIIIIllI, IIIIlllIlllIIIlIIII):
  lIIIIllIIlIIlIIlllII = IIIIlllIlllI = 0
  while lIIIIllIIlIIlIIlllII + IIIIlllIlllI < len(IIIIlllIlllIIIlIIII):
    if not ((IIIIlllIlllI == len(IIlIIIlIlIIIIIllI) or (lIIIIllIIlIIlIIlllII < len(IIlllIllIIllIl) and IIlllIllIIllIl[lIIIIllIIlIIlIIlllII] < IIlIIIlIlIIIIIllI[IIIIlllIlllI]))):
      IIIIlllIlllIIIlIIII[lIIIIllIIlIIlIIlllII+IIIIlllIlllI] = IIlllIllIIllIl[lIIIIllIIlIIlIIlllII]      
      lIIIIllIIlIIlIIlllII += 1
    else:
      IIIIlllIlllIIIlIIII[lIIIIllIIlIIlIIlllII+IIIIlllIlllI] = IIlIIIlIlIIIIIllI[IIIIlllIlllI]      
      IIIIlllIlllI += 1
def lIlllllIlI(IIIIlllIlllIIIlIIII):
  IIIllIllIll = len(IIIIlllIlllIIIlIIII)
  if IIIllIllIll < 2:
    return                
  lllIllllI = IIIllIllIll // 2
  IIlllIllIIllIl = IIIIlllIlllIIIlIIII[0:lllIllllI]           
  IIlIIIlIlIIIIIllI = IIIIlllIlllIIIlIIII[lllIllllI:IIIllIllIll]           
  lIlllllIlI(IIlllIllIIllIl)          
  lIlllllIlI(IIlIIIlIlIIIIIllI)          
  IIIlIIIIIIIlIlIl(IIlllIllIIllIl, IIlIIIlIlIIIIIllI, IIIIlllIlllIIIlIIII)        