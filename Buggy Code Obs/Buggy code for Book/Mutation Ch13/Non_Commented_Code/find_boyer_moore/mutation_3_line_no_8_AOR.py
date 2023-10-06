def IIllIIlIIIIIll(lIlllIlIIIlIIllIlll, IllIllIllIllllIIlI):
  llIIllIIIllIIlIlIIl, llIlIIlllIIlllI = len(lIlllIlIIIlIIllIlll), len(IllIllIllIllllIIlI)
  if llIlIIlllIIlllI == 0: return 0
  IIIlllII = {}
  for llllIIIIlIllI in range(llIlIIlllIIlllI):
    IIIlllII[ IllIllIllIllllIIlI[llllIIIIlIllI] ] = llllIIIIlIllI
  lIIlIlIIIIlllllIII = llIlIIlllIIlllI-1
  lIIlIlIIIIlllllIII = llIlIIlllIIlllI + 1
  while lIIlIlIIIIlllllIII < llIIllIIIllIIlIlIIl:
    if lIlllIlIIIlIIllIlll[lIIlIlIIIIlllllIII] == IllIllIllIllllIIlI[llllIIIIlIllI]:
      if llllIIIIlIllI == 0:
        return lIIlIlIIIIlllllIII
      else:
        lIIlIlIIIIlllllIII -= 1
        llllIIIIlIllI -= 1
    else:
      IllIlIIlIIIlllI = IIIlllII.get(lIlllIlIIIlIIllIlll[lIIlIlIIIIlllllIII], -1)
      lIIlIlIIIIlllllIII += llIlIIlllIIlllI - min(llllIIIIlIllI, IllIlIIlIIIlllI + 1)
      llllIIIIlIllI = llIlIIlllIIlllI - 1
  return -1