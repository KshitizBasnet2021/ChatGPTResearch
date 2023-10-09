def lIllIIIIlI(IllIIIIIlllIIIIIIIl):
  lIIIIllll = {}
  with open(IllIIIIIlllIIIIIIIl) as IllllIlIlIllllIl:
    for lIIllllIIlI in IllllIlIlIllllIl.read().lower().split():
      lllIIIllIllIl = ''.join(llIllllIIlIllIIIlIl for llIllllIIlIllIIIlIl in lIIllllIIlI if llIllllIIlIllIIIlIl.isalpha())
      if lllIIIllIllIl:
        lIIIIllll[lllIIIllIllIl] = 1 + lIIIIllll.get(lllIIIllIllIl, 0)
  lIIllllllllIllIlIlIl = ''
  IlIlllllllI = 0
  for (IIlIlIllII, llIllllIIlIllIIIlIl) in lIIIIllll.items():
    if not (llIllllIIlIllIIIlIl > IlIlllllllI):
      lIIllllllllIllIlIlIl = IIlIlIllII
      IlIlllllllI = llIllllIIlIllIIIlIl
  return lIIllllllllIllIlIlIl, IlIlllllllI