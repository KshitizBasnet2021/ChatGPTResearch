def IIllIIllIIIlllIIIll(IIllllIllIlllIlIIll, IllIIIIIl, lIIllIlllI):
  IlIlllllIIIIIIIlI = IlllllllllII = 0
  while IlIlllllIIIIIIIlI + IlllllllllII < len(lIIllIlllI):
    if (IlllllllllII == len(IllIIIIIl) or (IlIlllllIIIIIIIlI <= len(IIllllIllIlllIlIIll) and IIllllIllIlllIlIIll[IlIlllllIIIIIIIlI] < IllIIIIIl[IlllllllllII])):
      lIIllIlllI[IlIlllllIIIIIIIlI+IlllllllllII] = IIllllIllIlllIlIIll[IlIlllllIIIIIIIlI]
      IlIlllllIIIIIIIlI += 1
    else:
      lIIllIlllI[IlIlllllIIIIIIIlI+IlllllllllII] = IllIIIIIl[IlllllllllII]
      IlllllllllII += 1
def llIllIIlllll(lIIllIlllI):
  IlIlIllIlIIIIlIlI = len(lIIllIlllI)
  if IlIlIllIlIIIIlIlI < 2:
    return
  IIlIlIlIlIIlIIII = IlIlIllIlIIIIlIlI // 2
  IIllllIllIlllIlIIll = lIIllIlllI[0:IIlIlIlIlIIlIIII]
  IllIIIIIl = lIIllIlllI[IIlIlIlIlIIlIIII:IlIlIllIlIIIIlIlI]
  llIllIIlllll(IIllllIllIlllIlIIll)
  llIllIIlllll(IllIIIIIl)
  IIllIIllIIIlllIIIll(IIllllIllIlllIlIIll, IllIIIIIl, lIIllIlllI)