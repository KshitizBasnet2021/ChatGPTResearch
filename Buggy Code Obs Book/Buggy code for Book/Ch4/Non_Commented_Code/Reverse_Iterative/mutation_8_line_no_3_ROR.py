def IIIllIlIlIIllIl(lIIlllIIIllIlllIll):
  lIIlllIIIIlllIlIll, IllllIlIllll = 0, len(lIIlllIIIllIlllIll)
  while lIIlllIIIIlllIlIll <= IllllIlIllll - 1:
    lIIlllIIIllIlllIll[lIIlllIIIIlllIlIll], lIIlllIIIllIlllIll[IllllIlIllll-1] = lIIlllIIIllIlllIll[IllllIlIllll-1], lIIlllIIIllIlllIll[lIIlllIIIIlllIlIll]
    lIIlllIIIIlllIlIll, IllllIlIllll = lIIlllIIIIlllIlIll + 1, IllllIlIllll - 1