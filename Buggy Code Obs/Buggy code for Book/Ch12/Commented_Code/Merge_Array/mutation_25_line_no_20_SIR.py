def IllIlIlI(lIIllIIllIIlllllII, IlIIIIllIIIlII, lIlllllllIlIlIllllI):
  IlIlIlII = llIIlIlllllIIlIIllII = 0
  while IlIlIlII + llIIlIlllllIIlIIllII < len(lIlllllllIlIlIllllI):
    if llIIlIlllllIIlIIllII == len(IlIIIIllIIIlII) or (IlIlIlII < len(lIIllIIllIIlllllII) and lIIllIIllIIlllllII[IlIlIlII] < IlIIIIllIIIlII[llIIlIlllllIIlIIllII]):
      lIlllllllIlIlIllllI[IlIlIlII+llIIlIlllllIIlIIllII] = lIIllIIllIIlllllII[IlIlIlII]      
      IlIlIlII += 1
    else:
      lIlllllllIlIlIllllI[IlIlIlII+llIIlIlllllIIlIIllII] = IlIIIIllIIIlII[llIIlIlllllIIlIIllII]      
      llIIlIlllllIIlIIllII += 1
def IIIllIIIlIlIIlllII(lIlllllllIlIlIllllI):
  lIIIIIIllIl = len(lIlllllllIlIlIllllI)
  if lIIIIIIllIl < 2:
    return                
  IIIIIIlllllIlIl = lIIIIIIllIl // 2
  lIIllIIllIIlllllII = lIlllllllIlIlIllllI[0:IIIIIIlllllIlIl]           
  IlIIIIllIIIlII = lIlllllllIlIlIllllI[IIIIIIlllllIlIl:]
  IIIllIIIlIlIIlllII(lIIllIIllIIlllllII)          
  IIIllIIIlIlIIlllII(IlIIIIllIIIlII)          
  IllIlIlI(lIIllIIllIIlllllII, IlIIIIllIIIlII, lIlllllllIlIlIllllI)        