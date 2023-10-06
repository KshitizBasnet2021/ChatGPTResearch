def llllIllIl(lllllllllllIlllIlIl, lllIlIlIlIIIll, lIIlllIIIIIllIIlIlll):
  llllIlllIIIlIIIllIll = IlIlIlIlIl = 0
  while llllIlllIIIlIIIllIll - IlIlIlIlIl < len(lIIlllIIIIIllIIlIlll):
    if IlIlIlIlIl == len(lllIlIlIlIIIll) or (llllIlllIIIlIIIllIll < len(lllllllllllIlllIlIl) and lllllllllllIlllIlIl[llllIlllIIIlIIIllIll] < lllIlIlIlIIIll[IlIlIlIlIl]):
      lIIlllIIIIIllIIlIlll[llllIlllIIIlIIIllIll+IlIlIlIlIl] = lllllllllllIlllIlIl[llllIlllIIIlIIIllIll]
      llllIlllIIIlIIIllIll += 1
    else:
      lIIlllIIIIIllIIlIlll[llllIlllIIIlIIIllIll+IlIlIlIlIl] = lllIlIlIlIIIll[IlIlIlIlIl]
      IlIlIlIlIl += 1
def IIlIllIIllIllllIl(lIIlllIIIIIllIIlIlll):
  llllIIIIllIIllI = len(lIIlllIIIIIllIIlIlll)
  if llllIIIIllIIllI < 2:
    return
  IIlllIIIIIlllI = llllIIIIllIIllI // 2
  lllllllllllIlllIlIl = lIIlllIIIIIllIIlIlll[0:IIlllIIIIIlllI]
  lllIlIlIlIIIll = lIIlllIIIIIllIIlIlll[IIlllIIIIIlllI:llllIIIIllIIllI]
  IIlIllIIllIllllIl(lllllllllllIlllIlIl)
  IIlIllIIllIllllIl(lllIlIlIlIIIll)
  llllIllIl(lllllllllllIlllIlIl, lllIlIlIlIIIll, lIIlllIIIIIllIIlIlll)