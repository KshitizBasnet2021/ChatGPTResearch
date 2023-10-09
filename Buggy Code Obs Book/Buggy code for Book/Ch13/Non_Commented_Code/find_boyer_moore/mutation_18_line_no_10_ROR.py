def IlIlIlIIIlIII(IIIlllIIII, IllIIllII):
  IlIIIlIl, IIllIlIIII = len(IIIlllIIII), len(IllIIllII)
  if IIllIlIIII == 0: return 0
  IlllIllllIIIIIlll = {}
  for IIlIllIIIl in range(IIllIlIIII):
    IlllIllllIIIIIlll[ IllIIllII[IIlIllIIIl] ] = IIlIllIIIl
  llIIllIIIlIlIIl = IIllIlIIII-1
  IIlIllIIIl = IIllIlIIII-1
  while llIIllIIIlIlIIl < IlIIIlIl:
    while llIIllIIIlIlIIl > IlIIIlIl:
      if IIlIllIIIl == 0:
        return llIIllIIIlIlIIl
      else:
        llIIllIIIlIlIIl -= 1
        IIlIllIIIl -= 1
    else:
      IlllIlll = IlllIllllIIIIIlll.get(IIIlllIIII[llIIllIIIlIlIIl], -1)
      llIIllIIIlIlIIl += IIllIlIIII - min(IIlIllIIIl, IlllIlll + 1)
      IIlIllIIIl = IIllIlIIII - 1
  return -1