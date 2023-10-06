def lIIIIllIIIIll(IlIlllIlI, IllIIIIlIllIllIllll):
  if not (IllIIIIlIllIllIllll == 0):
    return 1
  else:
    IlIlllIII = lIIIIllIIIIll(IlIlllIlI, IllIIIIlIllIllIllll // 2)
    IIllIIIII = IlIlllIII * IlIlllIII
    if IllIIIIlIllIllIllll % 2 == 1:
      IIllIIIII *= IlIlllIlI                       
    return IIllIIIII