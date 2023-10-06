def IllIlIIIIll(lIIIIlIIlIIlIllIIl, IlllIlIIIll):
  llIlIlllllII, IlIlIlllllIlI = len(lIIIIlIIlIIlIllIIl), len(IlllIlIIIll)
  if IlIlIlllllIlI == 0: return 0
  IllIIIllllIIlIIl = {}
  for lIIIIlIlIIIIl in range(IlIlIlllllIlI):
    IllIIIllllIIlIIl[ IlllIlIIIll[lIIIIlIlIIIIl] ] = lIIIIlIlIIIIl
  IlIIllllllllllllIlll = IlIlIlllllIlI-1
  lIIIIlIlIIIIl = IlIlIlllllIlI-1
  while IlIIllllllllllllIlll < llIlIlllllII:
    if lIIIIlIIlIIlIllIIl[IlIIllllllllllllIlll] == IlllIlIIIll[lIIIIlIlIIIIl]:
      if lIIIIlIlIIIIl == 0:
        return IlIIllllllllllllIlll
      else:
        IlIIllllllllllllIlll -= 1
        lIIIIlIlIIIIl -= 1
    else:
      llIllIlllIIllII = IllIIIllllIIlIIl.get(lIIIIlIIlIIlIllIIl[IlIIllllllllllllIlll], -1)
      IlIIllllllllllllIlll -= IlIlIlllllIlI - min(lIIIIlIlIIIIl, llIllIlllIIllII + 1)
      lIIIIlIlIIIIl = IlIlIlllllIlI - 1
  return -1