def IIllllll(lIIIlllllIIlIIIllII, IlIllllIllIIllII, llIIlIIIllIllllIlll):
  lIIlIIlIlIIlIIlIllI = IIIlIlIIllIl = 0
  while lIIlIIlIlIIlIIlIllI + IIIlIlIIllIl < len(llIIlIIIllIllllIlll):
    if IIIlIlIIllIl == len(IlIllllIllIIllII) or (lIIlIIlIlIIlIIlIllI < len(lIIIlllllIIlIIIllII) and lIIIlllllIIlIIIllII[lIIlIIlIlIIlIIlIllI] < IlIllllIllIIllII[IIIlIlIIllIl]):
      llIIlIIIllIllllIlll[lIIlIIlIlIIlIIlIllI+IIIlIlIIllIl] = lIIIlllllIIlIIIllII[lIIlIIlIlIIlIIlIllI]
      lIIlIIlIlIIlIIlIllI += 1
    else:
      llIIlIIIllIllllIlll[lIIlIIlIlIIlIIlIllI+IIIlIlIIllIl] = IlIllllIllIIllII[IIIlIlIIllIl]
      IIIlIlIIllIl += 1
def lIIIlIlIIIllIIllI(llIIlIIIllIllllIlll):
  lIlIlIlI = len(llIIlIIIllIllllIlll)
  if lIlIlIlI < 2:
    return
  llIIlIllIlllIIlIl = lIlIlIlI // 2
  lIIIlllllIIlIIIllII = llIIlIIIllIllllIlll[0:llIIlIllIlllIIlIl]
  IlIllllIllIIllII = llIIlIIIllIllllIlll[llIIlIllIlllIIlIl:]
  lIIIlIlIIIllIIllI(lIIIlllllIIlIIIllII)
  lIIIlIlIIIllIIllI(IlIllllIllIIllII)
  IIllllll(lIIIlllllIIlIIIllII, IlIllllIllIIllII, llIIlIIIllIllllIlll)