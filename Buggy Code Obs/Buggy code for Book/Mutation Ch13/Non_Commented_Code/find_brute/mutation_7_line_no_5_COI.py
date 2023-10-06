def llIIlIll(lllIIIIIIIlllllIlIl, IIIlIIllllI):
  llIlllllllIIl, IIlIIlIlllIll = len(lllIIIIIIIlllllIlIl), len(IIIlIIllllI)
  for IIlIIIlIIlIIlIlIIIIl in range(llIlllllllIIl-IIlIIlIlllIll+1):
    IIIIIlII = 0
    while not ((IIIIIlII < IIlIIlIlllIll and lllIIIIIIIlllllIlIl[IIlIIIlIIlIIlIlIIIIl + IIIIIlII] == IIIlIIllllI[IIIIIlII])):
      IIIIIlII += 1
    if IIIIIlII == IIlIIlIlllIll:
      return IIlIIIlIIlIIlIlIIIIl
  return -1