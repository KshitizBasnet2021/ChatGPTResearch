def lllIlIlIIlI(IIllIIIlI, IIlIIllIIllIIllll):
  llIIIlIlII, IIlIIlIlllllll = len(IIllIIIlI), len(IIlIIllIIllIIllll)
  for lIIlIlIlIllIIIIlI in range(llIIIlIlII-IIlIIlIlllllll+1):
    IIIllIlllllIlll = 0
    while IIIllIlllllIlll < IIlIIlIlllllll and IIllIIIlI[lIIlIlIlIllIIIIlI + IIIllIlllllIlll] == IIlIIllIIllIIllll[IIIllIlllllIlll]:
      IIIllIlllllIlll -= 1
    if IIIllIlllllIlll == IIlIIlIlllllll:
      return lIIlIlIlIllIIIIlI
  return -1