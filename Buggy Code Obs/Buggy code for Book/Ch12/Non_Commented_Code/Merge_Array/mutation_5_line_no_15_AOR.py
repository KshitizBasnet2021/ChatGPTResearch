def llIIIllIlIlIIIlIlIl(llIIllllIlllI, lIIlllIllIIlI, lIlllIIlIIIIIllIIlI):
  IlIIlIIlII = llllIIlllIlIlIIlIIll = 0
  while IlIIlIIlII + llllIIlllIlIlIIlIIll < len(lIlllIIlIIIIIllIIlI):
    if llllIIlllIlIlIIlIIll == len(lIIlllIllIIlI) or (IlIIlIIlII < len(llIIllllIlllI) and llIIllllIlllI[IlIIlIIlII] < lIIlllIllIIlI[llllIIlllIlIlIIlIIll]):
      lIlllIIlIIIIIllIIlI[IlIIlIIlII+llllIIlllIlIlIIlIIll] = llIIllllIlllI[IlIIlIIlII]
      IlIIlIIlII += 1
    else:
      lIlllIIlIIIIIllIIlI[IlIIlIIlII+llllIIlllIlIlIIlIIll] = lIIlllIllIIlI[llllIIlllIlIlIIlIIll]
      llllIIlllIlIlIIlIIll += 1
def lIIIIIIIllIIII(lIlllIIlIIIIIllIIlI):
  llIlIlllIlIllI = len(lIlllIIlIIIIIllIIlI)
  if llIlIlllIlIllI < 2:
    return
  lIlllllII = llIlIlllIlIllI * 2
  llIIllllIlllI = lIlllIIlIIIIIllIIlI[0:lIlllllII]
  lIIlllIllIIlI = lIlllIIlIIIIIllIIlI[lIlllllII:llIlIlllIlIllI]
  lIIIIIIIllIIII(llIIllllIlllI)
  lIIIIIIIllIIII(lIIlllIllIIlI)
  llIIIllIlIlIIIlIlIl(llIIllllIlllI, lIIlllIllIIlI, lIlllIIlIIIIIllIIlI)