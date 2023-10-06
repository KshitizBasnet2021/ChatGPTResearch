def lIllllllIIllIlIllIl(lIlIlIlIIlIIIIIIllII, lIlllIIlllll):
  if lIlllIIlllll == 0:
    return 1
  else:
    IIllllIllIIllIIIIlll = lIllllllIIllIlIllIl(lIlIlIlIIlIIIIIIllII, lIlllIIlllll // 2)          
    llIlllllII = IIllllIllIIllIIIIlll * IIllllIllIIllIIIIlll
    if lIlllIIlllll % 2 != 1:
      llIlllllII *= lIlIlIlIIlIIIIIIllII                       
    return llIlllllII