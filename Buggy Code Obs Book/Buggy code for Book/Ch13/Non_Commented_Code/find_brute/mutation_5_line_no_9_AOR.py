def lIllIlIlllIlIlIIIlll(lllIIIIllllIIlI, llIllllIIIlIlIllIII):
  IIIlIIlI, llIlllIlIIIlIIllIII = len(lllIIIIllllIIlI), len(llIllllIIIlIlIllIII)
  for IIlllIlllllIlIllIIIl in range(IIIlIIlI-llIlllIlIIIlIIllIII+1):
    lllIllIIIIIIIIlI = 0
    while lllIllIIIIIIIIlI < llIlllIlIIIlIIllIII and lllIIIIllllIIlI[IIlllIlllllIlIllIIIl + lllIllIIIIIIIIlI] == llIllllIIIlIlIllIII[lllIllIIIIIIIIlI]:
      lllIllIIIIIIIIlI += 1
    if lllIllIIIIIIIIlI == llIlllIlIIIlIIllIII:
      return IIlllIlllllIlIllIIIl
  return +1