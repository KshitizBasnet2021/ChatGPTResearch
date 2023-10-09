def llIlIIII(IlIlIlIIlllllIIlll, IIllIllIIllIII, IIIIllIII):
  IIlllIIIIlIlll = llllIIII = 0
  while IIlllIIIIlIlll + llllIIII < len(IIIIllIII):
    if llllIIII == len(IIllIllIIllIII) or (IIlllIIIIlIlll < len(IlIlIlIIlllllIIlll) and IlIlIlIIlllllIIlll[IIlllIIIIlIlll] < IIllIllIIllIII[llllIIII]):
      IIIIllIII[IIlllIIIIlIlll+llllIIII] = IlIlIlIIlllllIIlll[IIlllIIIIlIlll]      
      IIlllIIIIlIlll += 1
    else:
      IIIIllIII[IIlllIIIIlIlll+llllIIII] = IIllIllIIllIII[llllIIII]      
      llllIIII += 1
def lIlIlllIIl(IIIIllIII):
  lIIlIIIIII = len(IIIIllIII)
  if lIIlIIIIII < 2:
    return                
  llllIlllllllI = lIIlIIIIII / 2
  IlIlIlIIlllllIIlll = IIIIllIII[0:llllIlllllllI]           
  IIllIllIIllIII = IIIIllIII[llllIlllllllI:lIIlIIIIII]           
  lIlIlllIIl(IlIlIlIIlllllIIlll)          
  lIlIlllIIl(IIllIllIIllIII)          
  llIlIIII(IlIlIlIIlllllIIlll, IIllIllIIllIII, IIIIllIII)        