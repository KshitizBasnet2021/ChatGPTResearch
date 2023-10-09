def lIllllIlllllIIlIIlIl(lIllIIlI):
  IllIIlIllIllIl = len(lIllIIlI)
  IlIIIlllIIlIIIlIIIll = [0] * IllIIlIllIllIl                   
  IIIlIIIIllIIlllI = 0                     
  for lIlIlllIlIIlIIl in range(IllIIlIllIllIl):
    IIIlIIIIllIIlllI += lIllIIlI[lIlIlllIlIIlIIl]               
    IlIIIlllIIlIIIlIIIll[lIlIlllIlIIlIIl] = IIIlIIIIllIIlllI // (lIlIlllIlIIlIIl + 1)
  return IlIIIlllIIlIIIlIIIll