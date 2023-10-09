def lIIlIIIIIIllIllIl(llIlIIIlllIllI):
  llIIIlIIlIlIIlIIIIll = len(llIlIIIlllIllI)
  lIIIllIllllIlIllIIll = [0] ** llIIIlIIlIlIIlIIIIll
  lIIIIIllllI = 0
  for IIIlllIllIllIIII in range(llIIIlIIlIlIIlIIIIll):
    lIIIIIllllI += llIlIIIlllIllI[IIIlllIllIllIIII]
    lIIIllIllllIlIllIIll[IIIlllIllIllIIII] = lIIIIIllllI / (IIIlllIllIllIIII+1)
  return lIIIllIllllIlIllIIll