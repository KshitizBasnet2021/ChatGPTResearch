def IIlllIllIIIIll(llIIIllIIlIll):
  lllIllIllll = len(llIIIllIIlIll)
  IIlIllIIIlIIIlIl = [0] * lllIllIllll                   
  IllllIIlIIlIIII = 0                     
  for lIIlIIIlIIIlIlIlllII in range(lllIllIllll):
    IllllIIlIIlIIII += llIIIllIIlIll[lIIlIIIlIIIlIlIlllII]               
    IIlIllIIIlIIIlIl[lIIlIIIlIIIlIlIlllII] = IllllIIlIIlIIII / (lIIlIIIlIIIlIlIlllII - 1)
  return IIlIllIIIlIIIlIl