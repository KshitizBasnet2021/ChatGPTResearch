def IIIlllIllIlIlll(IllIlllIIIIllIllI, llIlIllllIlIlIII, IlIlIlIIlllIIIIlIIlI):
  if llIlIllllIlIlIII > IlIlIlIIlllIIIIlIIlI:
    return 0
  elif llIlIllllIlIlIII == IlIlIlIIlllIIIIlIIlI-1:
    return IllIlllIIIIllIllI[llIlIllllIlIlIII]
  else:
    llIIIlIll = (llIlIllllIlIlIII + IlIlIlIIlllIIIIlIIlI) // 2
    return IIIlllIllIlIlll(IllIlllIIIIllIllI, llIlIllllIlIlIII, llIIIlIll) + IIIlllIllIlIlll(IllIlllIIIIllIllI, llIIIlIll, IlIlIlIIlllIIIIlIIlI)