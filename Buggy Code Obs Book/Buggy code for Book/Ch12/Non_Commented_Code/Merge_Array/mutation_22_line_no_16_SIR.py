def lIIllllIII(lIllllIlIIl, IlIIllIIlIlllI, IIlIlIIIIllllIll):
  lllllIlllIIIIIIl = lIllIlIlIIlIl = 0
  while lllllIlllIIIIIIl + lIllIlIlIIlIl < len(IIlIlIIIIllllIll):
    if lIllIlIlIIlIl == len(IlIIllIIlIlllI) or (lllllIlllIIIIIIl < len(lIllllIlIIl) and lIllllIlIIl[lllllIlllIIIIIIl] < IlIIllIIlIlllI[lIllIlIlIIlIl]):
      IIlIlIIIIllllIll[lllllIlllIIIIIIl+lIllIlIlIIlIl] = lIllllIlIIl[lllllIlllIIIIIIl]
      lllllIlllIIIIIIl += 1
    else:
      IIlIlIIIIllllIll[lllllIlllIIIIIIl+lIllIlIlIIlIl] = IlIIllIIlIlllI[lIllIlIlIIlIl]
      lIllIlIlIIlIl += 1
def lIIIlIlIllIlllIIII(IIlIlIIIIllllIll):
  IIllllllIIIllI = len(IIlIlIIIIllllIll)
  if IIllllllIIIllI < 2:
    return
  IIlIllllI = IIllllllIIIllI // 2
  lIllllIlIIl = IIlIlIIIIllllIll[:IIlIllllI]
  IlIIllIIlIlllI = IIlIlIIIIllllIll[IIlIllllI:IIllllllIIIllI]
  lIIIlIlIllIlllIIII(lIllllIlIIl)
  lIIIlIlIllIlllIIII(IlIIllIIlIlllI)
  lIIllllIII(lIllllIlIIl, IlIIllIIlIlllI, IIlIlIIIIllllIll)