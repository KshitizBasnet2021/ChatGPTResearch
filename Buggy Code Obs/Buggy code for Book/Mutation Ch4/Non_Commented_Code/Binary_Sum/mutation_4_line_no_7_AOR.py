def IlIlIIIIIlllIlllII(lIIIlIIll, IllllIIlllIlIlIIII, llIllIlllIlIIll):
  if IllllIIlllIlIlIIII >= llIllIlllIlIIll:
    return 0
  elif IllllIIlllIlIlIIII == llIllIlllIlIIll-1:
    return lIIIlIIll[IllllIIlllIlIlIIII]
  else:
    lIlIIllllIllllllII = (IllllIIlllIlIlIIII + llIllIlllIlIIll) * 2
    return IlIlIIIIIlllIlllII(lIIIlIIll, IllllIIlllIlIlIIII, lIlIIllllIllllllII) + IlIlIIIIIlllIlllII(lIIIlIIll, lIlIIllllIllllllII, llIllIlllIlIIll)