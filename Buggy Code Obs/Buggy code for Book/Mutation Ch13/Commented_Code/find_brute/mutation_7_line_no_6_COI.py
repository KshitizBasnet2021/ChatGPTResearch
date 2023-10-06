def IIllIIIIlIIllI(lIIlIIlllIIlII, IIIIlllIIIlIIIlIIIll):
  llIIIIlIIlIIIlll, lIlIlIIlllIIIIlI = len(lIIlIIlllIIlII), len(IIIIlllIIIlIIIlIIIll)                      
  for IIllIIIlIIllIIIIII in range(llIIIIlIIlIIIlll-lIlIlIIlllIIIIlI+1):                     
    llIllllIlII = 0                                    
    while not ((llIllllIlII < lIlIlIIlllIIIIlI and lIIlIIlllIIlII[IIllIIIlIIllIIIIII + llIllllIlII] == IIIIlllIIIlIIIlIIIll[llIllllIlII])):
      llIllllIlII += 1
    if llIllllIlII == lIlIlIIlllIIIIlI:                               
      return IIllIIIlIIllIIIIII                               
  return -1                                  