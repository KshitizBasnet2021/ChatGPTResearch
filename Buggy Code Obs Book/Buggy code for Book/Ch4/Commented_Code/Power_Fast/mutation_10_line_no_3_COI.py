def lIIIlIlllllIIIlIlI(IIIllIllIIlIlIlIIIl, IIllIIIII):
  if not (IIllIIIII == 0):
    return 1
  else:
    lIlIIllIl = lIIIlIlllllIIIlIlI(IIIllIllIIlIlIlIIIl, IIllIIIII // 2)          
    IlIllIII = lIlIIllIl * lIlIIllIl
    if IIllIIIII % 2 == 1:                      
      IlIllIII *= IIIllIllIIlIlIlIIIl                       
    return IlIllIII