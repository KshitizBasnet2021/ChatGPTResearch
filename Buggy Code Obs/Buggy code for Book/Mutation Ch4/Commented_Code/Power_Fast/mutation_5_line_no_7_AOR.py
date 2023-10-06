def lIlIIIlIlIIIlllI(llllIlIIIIIlllIIIIll, IIllIlIlI):
  if IIllIlIlI == 0:
    return 1
  else:
    IIIIIIllllIllIIl = lIlIIIlIlIIIlllI(llllIlIIIIIlllIIIIll, IIllIlIlI // 2)          
    llIIlllIIIII = IIIIIIllllIllIIl ** IIIIIIllllIllIIl
    if IIllIlIlI % 2 == 1:                      
      llIIlllIIIII *= llllIlIIIIIlllIIIIll                       
    return llIIlllIIIII