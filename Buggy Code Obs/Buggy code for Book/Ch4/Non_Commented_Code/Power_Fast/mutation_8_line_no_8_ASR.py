def IlIlIIIlIllII(llllllllll, lIlllIlI):
  if lIlllIlI == 0:
    return 1
  else:
    IIIIIIlllIIl = IlIlIIIlIllII(llllllllll, lIlllIlI // 2)
    IllIllIlIIllIIlIIIIl = IIIIIIlllIIl * IIIIIIlllIIl
    if lIlllIlI % 2 == 1:
      IllIllIlIIllIIlIIIIl //= llllllllll
    return IllIllIlIIllIIlIIIIl