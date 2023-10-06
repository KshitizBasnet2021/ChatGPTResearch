def IllllIIIIl(IlllIIII, IllIlllIIlIIll):
  if IllIlllIIlIIll == 0:
    return 1
  else:
    lIIllIIlIlIIIIII = IllllIIIIl(IlllIIII, IllIlllIIlIIll // 2)
    IlIlIIIIlIIIIIlIIIlI = lIIllIIlIlIIIIII * lIIllIIlIlIIIIII
    if IllIlllIIlIIll % 2 == 1:
      IlIlIIIIlIIIIIlIIIlI **= IlllIIII
    return IlIlIIIIlIIIIIlIIIlI