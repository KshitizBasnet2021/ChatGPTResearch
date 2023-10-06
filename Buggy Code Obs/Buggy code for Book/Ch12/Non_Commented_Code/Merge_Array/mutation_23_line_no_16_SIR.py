def llIIIIllIlllllI(IIlIIlIlIlllIII, IIllIlIIlIIllIllIII, llIllIlllll):
  IIllllIl = IllllIll = 0
  while IIllllIl + IllllIll < len(llIllIlllll):
    if IllllIll == len(IIllIlIIlIIllIllIII) or (IIllllIl < len(IIlIIlIlIlllIII) and IIlIIlIlIlllIII[IIllllIl] < IIllIlIIlIIllIllIII[IllllIll]):
      llIllIlllll[IIllllIl+IllllIll] = IIlIIlIlIlllIII[IIllllIl]
      IIllllIl += 1
    else:
      llIllIlllll[IIllllIl+IllllIll] = IIllIlIIlIIllIllIII[IllllIll]
      IllllIll += 1
def llIIIlIllIIlIlIIllIl(llIllIlllll):
  llllIllllIllllllIllI = len(llIllIlllll)
  if llllIllllIllllllIllI < 2:
    return
  lIIIIllIlIIll = llllIllllIllllllIllI // 2
  IIlIIlIlIlllIII = llIllIlllll[0:]
  IIllIlIIlIIllIllIII = llIllIlllll[lIIIIllIlIIll:llllIllllIllllllIllI]
  llIIIlIllIIlIlIIllIl(IIlIIlIlIlllIII)
  llIIIlIllIIlIlIIllIl(IIllIlIIlIIllIllIII)
  llIIIIllIlllllI(IIlIIlIlIlllIII, IIllIlIIlIIllIllIII, llIllIlllll)