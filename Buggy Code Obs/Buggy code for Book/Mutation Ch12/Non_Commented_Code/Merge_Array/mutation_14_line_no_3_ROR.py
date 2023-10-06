def IIIIlIllIIlllllll(IlllIlIlIIIlIlIll, llllllIIIllIlIIIll, IllllIIIIllIIllI):
  IIlllIlIlllllIlIIlIl = llIlIllI = 0
  while IIlllIlIlllllIlIIlIl + llIlIllI <= len(IllllIIIIllIIllI):
    if llIlIllI == len(llllllIIIllIlIIIll) or (IIlllIlIlllllIlIIlIl < len(IlllIlIlIIIlIlIll) and IlllIlIlIIIlIlIll[IIlllIlIlllllIlIIlIl] < llllllIIIllIlIIIll[llIlIllI]):
      IllllIIIIllIIllI[IIlllIlIlllllIlIIlIl+llIlIllI] = IlllIlIlIIIlIlIll[IIlllIlIlllllIlIIlIl]
      IIlllIlIlllllIlIIlIl += 1
    else:
      IllllIIIIllIIllI[IIlllIlIlllllIlIIlIl+llIlIllI] = llllllIIIllIlIIIll[llIlIllI]
      llIlIllI += 1
def lIIlllllIIIlIIlIII(IllllIIIIllIIllI):
  IIlIlIllIIllIllIlll = len(IllllIIIIllIIllI)
  if IIlIlIllIIllIllIlll < 2:
    return
  lllllIlIIlllIIllIlII = IIlIlIllIIllIllIlll // 2
  IlllIlIlIIIlIlIll = IllllIIIIllIIllI[0:lllllIlIIlllIIllIlII]
  llllllIIIllIlIIIll = IllllIIIIllIIllI[lllllIlIIlllIIllIlII:IIlIlIllIIllIllIlll]
  lIIlllllIIIlIIlIII(IlllIlIlIIIlIlIll)
  lIIlllllIIIlIIlIII(llllllIIIllIlIIIll)
  IIIIlIllIIlllllll(IlllIlIlIIIlIlIll, llllllIIIllIlIIIll, IllllIIIIllIIllI)