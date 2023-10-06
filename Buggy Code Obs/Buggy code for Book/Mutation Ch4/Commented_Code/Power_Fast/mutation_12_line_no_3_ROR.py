def llIllIlllIlIl(lIIIIlIIllllllllIlII, lllllIIll):
  if lllllIIll != 0:
    return 1
  else:
    IIlIIIlIII = llIllIlllIlIl(lIIIIlIIllllllllIlII, lllllIIll // 2)          
    IlIIlIlIllI = IIlIIIlIII * IIlIIIlIII
    if lllllIIll % 2 == 1:                      
      IlIIlIlIllI *= lIIIIlIIllllllllIlII                       
    return IlIIlIlIllI