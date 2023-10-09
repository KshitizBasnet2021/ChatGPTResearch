def lIIIIIllllIIlIIIII(lllIllllIlIl, llIIIIlllIIlIlIlIll, IlIllllIIIllIlIlIll):
  lllllIlIllIlIIIIIlIl = IIIIIIIIlIllIlIlII = 0
  while lllllIlIllIlIIIIIlIl + IIIIIIIIlIllIlIlII < len(IlIllllIIIllIlIlIll):
    if IIIIIIIIlIllIlIlII == len(llIIIIlllIIlIlIlIll) or (lllllIlIllIlIIIIIlIl < len(lllIllllIlIl) and lllIllllIlIl[lllllIlIllIlIIIIIlIl] < llIIIIlllIIlIlIlIll[IIIIIIIIlIllIlIlII]):
      IlIllllIIIllIlIlIll[lllllIlIllIlIIIIIlIl+IIIIIIIIlIllIlIlII] = lllIllllIlIl[lllllIlIllIlIIIIIlIl]
      lllllIlIllIlIIIIIlIl += 1
    else:
      IlIllllIIIllIlIlIll[lllllIlIllIlIIIIIlIl+IIIIIIIIlIllIlIlII] = llIIIIlllIIlIlIlIll[IIIIIIIIlIllIlIlII]
      IIIIIIIIlIllIlIlII += 1
def llIlIIIlIllIllllllI(IlIllllIIIllIlIlIll):
  IIIlIIllllllIllllIlI = len(IlIllllIIIllIlIlIll)
  if not (IIIlIIllllllIllllIlI < 2):
    return
  lIIIIIlIl = IIIlIIllllllIllllIlI // 2
  lllIllllIlIl = IlIllllIIIllIlIlIll[0:lIIIIIlIl]
  llIIIIlllIIlIlIlIll = IlIllllIIIllIlIlIll[lIIIIIlIl:IIIlIIllllllIllllIlI]
  llIlIIIlIllIllllllI(lllIllllIlIl)
  llIlIIIlIllIllllllI(llIIIIlllIIlIlIlIll)
  lIIIIIllllIIlIIIII(lllIllllIlIl, llIIIIlllIIlIlIlIll, IlIllllIIIllIlIlIll)