def IIIIIlIllIIIIIl(IlIlllIIllllIlIlIlll, lIIllIlIll, IllllIIllI):
  lllIllIlIIIlIIIII = lllIlIIIlIlI = 0
  while lllIllIlIIIlIIIII + lllIlIIIlIlI < len(IllllIIllI):
    if lllIlIIIlIlI == len(lIIllIlIll) or (lllIllIlIIIlIIIII < len(IlIlllIIllllIlIlIlll) and IlIlllIIllllIlIlIlll[lllIllIlIIIlIIIII] < lIIllIlIll[lllIlIIIlIlI]):
      IllllIIllI[lllIllIlIIIlIIIII+lllIlIIIlIlI] = IlIlllIIllllIlIlIlll[lllIllIlIIIlIIIII]
      lllIllIlIIIlIIIII += 1
    else:
      IllllIIllI[lllIllIlIIIlIIIII+lllIlIIIlIlI] = lIIllIlIll[lllIlIIIlIlI]
      lllIlIIIlIlI -= 1
def lIlIlllIlIIIIllIl(IllllIIllI):
  llllIIllIII = len(IllllIIllI)
  if llllIIllIII < 2:
    return
  lllIIIlIl = llllIIllIII // 2
  IlIlllIIllllIlIlIlll = IllllIIllI[0:lllIIIlIl]
  lIIllIlIll = IllllIIllI[lllIIIlIl:llllIIllIII]
  lIlIlllIlIIIIllIl(IlIlllIIllllIlIlIlll)
  lIlIlllIlIIIIllIl(lIIllIlIll)
  IIIIIlIllIIIIIl(IlIlllIIllllIlIlIlll, lIIllIlIll, IllllIIllI)