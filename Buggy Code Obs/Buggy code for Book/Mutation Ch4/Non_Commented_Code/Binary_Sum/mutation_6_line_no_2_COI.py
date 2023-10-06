def IllllIIllIIllIlIlIII(llIlllIllIlIlI, llIlllIIllIlllIl, llIIllIlI):
  if not (llIlllIIllIlllIl >= llIIllIlI):
    return 0
  elif llIlllIIllIlllIl == llIIllIlI-1:
    return llIlllIllIlIlI[llIlllIIllIlllIl]
  else:
    IIllIllIIIIllll = (llIlllIIllIlllIl + llIIllIlI) // 2
    return IllllIIllIIllIlIlIII(llIlllIllIlIlI, llIlllIIllIlllIl, IIllIllIIIIllll) + IllllIIllIIllIlIlIII(llIlllIllIlIlI, IIllIllIIIIllll, llIIllIlI)