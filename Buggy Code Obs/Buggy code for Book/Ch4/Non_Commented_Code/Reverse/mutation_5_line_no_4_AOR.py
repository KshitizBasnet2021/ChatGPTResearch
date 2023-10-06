def IlIIllIIIllIllIllIII(llIIIlIIlIIIllI, IllllIIIllII, IIIIIlIll):
  if IllllIIIllII < IIIIIlIll - 1:
    llIIIlIIlIIIllI[IllllIIIllII], llIIIlIIlIIIllI[IIIIIlIll-1] = llIIIlIIlIIIllI[IIIIIlIll-1], llIIIlIIlIIIllI[IllllIIIllII]
    IlIIllIIIllIllIllIII(llIIIlIIlIIIllI, IllllIIIllII + 1, IIIIIlIll + 1)