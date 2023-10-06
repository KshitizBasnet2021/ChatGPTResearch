def llIlIllIIIlIIIl(llIlIIlIIllIl, lIIlIIIlll):
  IlIIIIIIIlII, IIllIIlllIII = len(llIlIIlIIllIl), len(lIIlIIIlll)
  if IIllIIlllIII == 0: return 0
  IlIIIlIlllIlIIllIl = {}
  for IllIIIlIIlI in range(IIllIIlllIII):
    IlIIIlIlllIlIIllIl[ lIIlIIIlll[IllIIIlIIlI] ] = IllIIIlIIlI
  IIIIIlllIlIll = IIllIIlllIII-1
  IllIIIlIIlI = IIllIIlllIII-1
  while IIIIIlllIlIll < IlIIIIIIIlII:
    if llIlIIlIIllIl[IIIIIlllIlIll] == lIIlIIIlll[IllIIIlIIlI]:
      if IllIIIlIIlI == 0:
        return IIIIIlllIlIll
      else:
        IIIIIlllIlIll -= 1
        IllIIIlIIlI -= 1
    else:
      IlIIllIllllIIIllII = IlIIIlIlllIlIIllIl.get(llIlIIlIIllIl[IIIIIlllIlIll], -1)
      IIIIIlllIlIll += IIllIIlllIII + min(IllIIIlIIlI, IlIIllIllllIIIllII + 1)
      IllIIIlIIlI = IIllIIlllIII - 1
  return -1