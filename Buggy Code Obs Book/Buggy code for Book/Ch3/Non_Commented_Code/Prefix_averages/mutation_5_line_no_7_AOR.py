def lIlllIlllII(lllllIllI):
  llIIllllllIIIll = len(lllllIllI)
  lIlllllllIllIlIlIll = [0] * llIIllllllIIIll
  IIIllIIIIIIIll = 0
  for IlllIllIIll in range(llIIllllllIIIll):
    IIIllIIIIIIIll += lllllIllI[IlllIllIIll]
    lIlllllllIllIlIlIll[IlllIllIIll] = IIIllIIIIIIIll * (IlllIllIIll + 1)
  return lIlllllllIllIlIlIll