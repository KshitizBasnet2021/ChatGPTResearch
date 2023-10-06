def lIlIlllIlIIllIIlllll(IIlIIIllIllIlIllllIl, lllIllIlIIllIIlIIlI, IIIIIlIllIllIlIlllIl):
  IlIIlllllIlI = IIllIllIlIIllII = 0
  while IlIIlllllIlI + IIllIllIlIIllII < len(IIIIIlIllIllIlIlllIl):
    if IIllIllIlIIllII == len(lllIllIlIIllIIlIIlI) or (IlIIlllllIlI < len(IIlIIIllIllIlIllllIl) and IIlIIIllIllIlIllllIl[IlIIlllllIlI] < lllIllIlIIllIIlIIlI[IIllIllIlIIllII]):
      IIIIIlIllIllIlIlllIl[IlIIlllllIlI+IIllIllIlIIllII] = IIlIIIllIllIlIllllIl[IlIIlllllIlI]      
      IlIIlllllIlI += 1
    else:
      IIIIIlIllIllIlIlllIl[IlIIlllllIlI+IIllIllIlIIllII] = lllIllIlIIllIIlIIlI[IIllIllIlIIllII]      
      IIllIllIlIIllII += 1
def IllllIllllIllII(IIIIIlIllIllIlIlllIl):
  IIIllIlIlI = len(IIIIIlIllIllIlIlllIl)
  if IIIllIlIlI < 2:
    return                
  llIIIIlIllIllIIlI = IIIllIlIlI // 2
  IIlIIIllIllIlIllllIl = IIIIIlIllIllIlIlllIl[:llIIIIlIllIllIIlI]
  lllIllIlIIllIIlIIlI = IIIIIlIllIllIlIlllIl[llIIIIlIllIllIIlI:IIIllIlIlI]           
  IllllIllllIllII(IIlIIIllIllIlIllllIl)          
  IllllIllllIllII(lllIllIlIIllIIlIIlI)          
  lIlIlllIlIIllIIlllll(IIlIIIllIllIlIllllIl, lllIllIlIIllIIlIIlI, IIIIIlIllIllIlIlllIl)        