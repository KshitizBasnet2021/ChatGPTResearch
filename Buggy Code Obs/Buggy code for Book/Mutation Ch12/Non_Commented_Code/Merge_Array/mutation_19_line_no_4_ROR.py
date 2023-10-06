def lllIIIlllIlIllIl(IllllIIIlI, llIIIIlIlIIlIllllll, lIIlIlIlllIll):
  llIlllllII = IIIIllIlIllIl = 0
  while llIlllllII + IIIIllIlIllIl < len(lIIlIlIlllIll):
    if (IIIIllIlIllIl == len(llIIIIlIlIIlIllllll) or (llIlllllII < len(IllllIIIlI) and IllllIIIlI[llIlllllII] <= llIIIIlIlIIlIllllll[IIIIllIlIllIl])):
      lIIlIlIlllIll[llIlllllII+IIIIllIlIllIl] = IllllIIIlI[llIlllllII]
      llIlllllII += 1
    else:
      lIIlIlIlllIll[llIlllllII+IIIIllIlIllIl] = llIIIIlIlIIlIllllll[IIIIllIlIllIl]
      IIIIllIlIllIl += 1
def llIIllllIIlllll(lIIlIlIlllIll):
  llIlllIIIIlIIlll = len(lIIlIlIlllIll)
  if llIlllIIIIlIIlll < 2:
    return
  IIlIIIlllllIlIIIIl = llIlllIIIIlIIlll // 2
  IllllIIIlI = lIIlIlIlllIll[0:IIlIIIlllllIlIIIIl]
  llIIIIlIlIIlIllllll = lIIlIlIlllIll[IIlIIIlllllIlIIIIl:llIlllIIIIlIIlll]
  llIIllllIIlllll(IllllIIIlI)
  llIIllllIIlllll(llIIIIlIlIIlIllllll)
  lllIIIlllIlIllIl(IllllIIIlI, llIIIIlIlIIlIllllll, lIIlIlIlllIll)