def IIlIlllII(IlIIllllI):
  IIIIIIllIIllIIIlI, IIIIIIIlIllIIllIlll = 0, len(IlIIllllI)
  while not (IIIIIIllIIllIIIlI < IIIIIIIlIllIIllIlll - 1):
    IlIIllllI[IIIIIIllIIllIIIlI], IlIIllllI[IIIIIIIlIllIIllIlll-1] = IlIIllllI[IIIIIIIlIllIIllIlll-1], IlIIllllI[IIIIIIllIIllIIIlI]  
    IIIIIIllIIllIIIlI, IIIIIIIlIllIIllIlll = IIIIIIllIIllIIIlI + 1, IIIIIIIlIllIIllIlll - 1          