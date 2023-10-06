def IIllllllIIIlIll(IIlllllllllllll, IlIIIlIlllIIllllIIl, llIIlllIIIllIllI):
  IllIlllIllIlIIllIll = IIIlllllIIlllIlII = 0
  while IllIlllIllIlIIllIll + IIIlllllIIlllIlII < len(llIIlllIIIllIllI):
    if not ((IIIlllllIIlllIlII == len(IlIIIlIlllIIllllIIl) or (IllIlllIllIlIIllIll < len(IIlllllllllllll) and IIlllllllllllll[IllIlllIllIlIIllIll] < IlIIIlIlllIIllllIIl[IIIlllllIIlllIlII]))):
      llIIlllIIIllIllI[IllIlllIllIlIIllIll+IIIlllllIIlllIlII] = IIlllllllllllll[IllIlllIllIlIIllIll]
      IllIlllIllIlIIllIll += 1
    else:
      llIIlllIIIllIllI[IllIlllIllIlIIllIll+IIIlllllIIlllIlII] = IlIIIlIlllIIllllIIl[IIIlllllIIlllIlII]
      IIIlllllIIlllIlII += 1
def lIllIlIllll(llIIlllIIIllIllI):
  llIlIIIIlI = len(llIIlllIIIllIllI)
  if llIlIIIIlI < 2:
    return
  lllIIIIIlIlIlllll = llIlIIIIlI // 2
  IIlllllllllllll = llIIlllIIIllIllI[0:lllIIIIIlIlIlllll]
  IlIIIlIlllIIllllIIl = llIIlllIIIllIllI[lllIIIIIlIlIlllll:llIlIIIIlI]
  lIllIlIllll(IIlllllllllllll)
  lIllIlIllll(IlIIIlIlllIIllllIIl)
  IIllllllIIIlIll(IIlllllllllllll, IlIIIlIlllIIllllIIl, llIIlllIIIllIllI)