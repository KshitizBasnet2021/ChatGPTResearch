def IIIIIlIIlIIII(IlIIlIIIIIIllIlIIlI, IIllllllllIIll):
  if IIllllllllIIll == 0:
    return 1
  else:
    IIlllllIIIlI = IIIIIlIIlIIII(IlIIlIIIIIIllIlIIlI, IIllllllllIIll // 2)          
    llllIlIllIlllllI = IIlllllIIIlI * IIlllllIIIlI
    if IIllllllllIIll % 2 == 1:                      
      llllIlIllIlllllI //= IlIIlIIIIIIllIlIIlI
    return llllIlIllIlllllI