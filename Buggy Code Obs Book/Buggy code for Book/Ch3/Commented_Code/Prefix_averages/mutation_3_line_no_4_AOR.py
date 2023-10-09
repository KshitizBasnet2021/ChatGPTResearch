def IlllIIIIIIlllIlIlllI(lIIlllIlIlIlllllllI):
  llIlllIlIIlIIlll = len(lIIlllIlIlIlllllllI)
  lIlIIIIlIllIIlIIIII = [0] ** llIlllIlIIlIIlll
  lIIllIIlIIllIIIIIlII = 0                     
  for IIlllIlIlIlIIlIl in range(llIlllIlIIlIIlll):
    lIIllIIlIIllIIIIIlII += lIIlllIlIlIlllllllI[IIlllIlIlIlIIlIl]               
    lIlIIIIlIllIIlIIIII[IIlllIlIlIlIIlIl] = lIIllIIlIIllIIIIIlII / (IIlllIlIlIlIIlIl+1)        
  return lIlIIIIlIllIIlIIIII