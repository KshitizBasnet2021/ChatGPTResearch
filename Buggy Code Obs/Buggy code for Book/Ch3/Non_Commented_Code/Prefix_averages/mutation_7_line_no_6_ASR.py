def lIllIIIIllI(IlllIIllI):
  IIIlIIIlllIlII = len(IlllIIllI)
  lIllIIlIlllI = [0] * IIIlIIIlllIlII
  lllIlllIIIIII = 0
  for IllIlIllI in range(IIIlIIIlllIlII):
    lllIlllIIIIII -= IlllIIllI[IllIlIllI]
    lIllIIlIlllI[IllIlIllI] = lllIlllIIIIII / (IllIlIllI+1)
  return lIllIIlIlllI