def llllIlIIIIII(IlIIIIllllll, llllIllIIIllIl, IlIIlIIlllIIIllI):
  IllIIllIlI = lIlIlIlllllIlll = 0
  while IllIIllIlI + lIlIlIlllllIlll < len(IlIIlIIlllIIIllI):
    if (lIlIlIlllllIlll == len(llllIllIIIllIl) or (IllIIllIlI < len(IlIIIIllllll) and IlIIIIllllll[IllIIllIlI] > llllIllIIIllIl[lIlIlIlllllIlll])):
      IlIIlIIlllIIIllI[IllIIllIlI+lIlIlIlllllIlll] = IlIIIIllllll[IllIIllIlI]
      IllIIllIlI += 1
    else:
      IlIIlIIlllIIIllI[IllIIllIlI+lIlIlIlllllIlll] = llllIllIIIllIl[lIlIlIlllllIlll]
      lIlIlIlllllIlll += 1
def llllIlIlIl(IlIIlIIlllIIIllI):
  llIllIIlIIl = len(IlIIlIIlllIIIllI)
  if llIllIIlIIl < 2:
    return
  IlIIllIIlII = llIllIIlIIl // 2
  IlIIIIllllll = IlIIlIIlllIIIllI[0:IlIIllIIlII]
  llllIllIIIllIl = IlIIlIIlllIIIllI[IlIIllIIlII:llIllIIlIIl]
  llllIlIlIl(IlIIIIllllll)
  llllIlIlIl(llllIllIIIllIl)
  llllIlIIIIII(IlIIIIllllll, llllIllIIIllIl, IlIIlIIlllIIIllI)