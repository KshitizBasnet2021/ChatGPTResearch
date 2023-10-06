def IIllIIlIIIIllI(llllIllIlllII):
  for IlIlllIlIlIllllI in range(1, len(llllIllIlllII)):
    IIlIIllIIlIlllIIIIII = llllIllIlllII[IlIlllIlIlIllllI]
    IIllllllIIllIllllll = IlIlllIlIlIllllI
    while IIllllllIIllIllllll > 0 and llllIllIlllII[IIllllllIIllIllllll-1] > IIlIIllIIlIlllIIIIII:
      llllIllIlllII[IIllllllIIllIllllll] = llllIllIlllII[IIllllllIIllIllllll-1]
      IIllllllIIllIllllll += 1
    llllIllIlllII[IIllllllIIllIllllll] = IIlIIllIIlIlllIIIIII