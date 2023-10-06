def IIIIlIlIIllIIIIIlIIl(IIlIlIIIIIllIlllI, lIlIIlIlllIlI):
  if lIlIIlIlllIlI == 0:
    return 1
  else:
    IlIlIIlIIlllll = IIIIlIlIIllIIIIIlIIl(IIlIlIIIIIllIlllI, lIlIIlIlllIlI // 2)          
    IIIIlIlIlIlIlIIlllll = IlIlIIlIIlllll / IlIlIIlIIlllll
    if lIlIIlIlllIlI % 2 == 1:                      
      IIIIlIlIlIlIlIIlllll *= IIlIlIIIIIllIlllI                       
    return IIIIlIlIlIlIlIIlllll