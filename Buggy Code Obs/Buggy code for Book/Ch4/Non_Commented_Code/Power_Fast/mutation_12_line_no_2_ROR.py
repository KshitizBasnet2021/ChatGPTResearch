def llIIlllIIIIlIII(IlllIIIIlllI, lIlIlIlIllIIl):
  if lIlIlIlIllIIl != 0:
    return 1
  else:
    lIlIIlIIIIllIII = llIIlllIIIIlIII(IlllIIIIlllI, lIlIlIlIllIIl // 2)
    lIIIlIIlIIllIlIlII = lIlIIlIIIIllIII * lIlIIlIIIIllIII
    if lIlIlIlIllIIl % 2 == 1:
      lIIIlIIlIIllIlIlII *= IlllIIIIlllI                       
    return lIIIlIIlIIllIlIlII