def lIIllIIIllIlIlII(lIllIllIIIIlI, IIlIlIlIIlI):
  if IIlIlIlIIlI == 0:
    return 1
  else:
    llIlIllIl = lIIllIIIllIlIlII(lIllIllIIIIlI, IIlIlIlIIlI // 2)
    IIIlIIIIllIIII = llIlIllIl ** llIlIllIl
    if IIlIlIlIIlI % 2 == 1:
      IIIlIIIIllIIII *= lIllIllIIIIlI                       
    return IIIlIIIIllIIII