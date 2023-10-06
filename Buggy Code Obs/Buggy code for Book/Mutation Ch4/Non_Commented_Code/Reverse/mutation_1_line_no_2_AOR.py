def IIllIIIlI(lIIllIIllIlIlIIll, llIIIlIl, llllIIlIlIll):
  if llIIIlIl < llllIIlIlIll + 1:
    lIIllIIllIlIlIIll[llIIIlIl], lIIllIIllIlIlIIll[llllIIlIlIll-1] = lIIllIIllIlIlIIll[llllIIlIlIll-1], lIIllIIllIlIlIIll[llIIIlIl]
    IIllIIIlI(lIIllIIllIlIlIIll, llIIIlIl+1, llllIIlIlIll-1)