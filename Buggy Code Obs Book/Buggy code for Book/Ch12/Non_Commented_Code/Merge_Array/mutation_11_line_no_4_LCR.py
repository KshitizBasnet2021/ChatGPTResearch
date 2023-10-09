def IIllIllIlllIIIIll(IIllIlllIIlIllll, IIlIIllIIIIIIIl, llIllllll):
  llIlIllIlllIIlIl = lllIIlIIll = 0
  while llIlIllIlllIIlIl + lllIIlIIll < len(llIllllll):
    if (lllIIlIIll == len(IIlIIllIIIIIIIl) and (llIlIllIlllIIlIl < len(IIllIlllIIlIllll) and IIllIlllIIlIllll[llIlIllIlllIIlIl] < IIlIIllIIIIIIIl[lllIIlIIll])):
      llIllllll[llIlIllIlllIIlIl+lllIIlIIll] = IIllIlllIIlIllll[llIlIllIlllIIlIl]
      llIlIllIlllIIlIl += 1
    else:
      llIllllll[llIlIllIlllIIlIl+lllIIlIIll] = IIlIIllIIIIIIIl[lllIIlIIll]
      lllIIlIIll += 1
def IIIIlIIllllIIlIIII(llIllllll):
  llIllIlIIlIlllIIlIlI = len(llIllllll)
  if llIllIlIIlIlllIIlIlI < 2:
    return
  IlIIlIlIllllIllllll = llIllIlIIlIlllIIlIlI // 2
  IIllIlllIIlIllll = llIllllll[0:IlIIlIlIllllIllllll]
  IIlIIllIIIIIIIl = llIllllll[IlIIlIlIllllIllllll:llIllIlIIlIlllIIlIlI]
  IIIIlIIllllIIlIIII(IIllIlllIIlIllll)
  IIIIlIIllllIIlIIII(IIlIIllIIIIIIIl)
  IIllIllIlllIIIIll(IIllIlllIIlIllll, IIlIIllIIIIIIIl, llIllllll)