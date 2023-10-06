def IllIlllllllIllll(IIlIIllIIIIlIl, IllIIIlllllIlllIlI, IIlIIllIlII):
  lllIIIlIlllIlIlII = IlIllllIIlII = 0
  while lllIIIlIlllIlIlII - IlIllllIIlII < len(IIlIIllIlII):
    if IlIllllIIlII == len(IllIIIlllllIlllIlI) or (lllIIIlIlllIlIlII < len(IIlIIllIIIIlIl) and IIlIIllIIIIlIl[lllIIIlIlllIlIlII] < IllIIIlllllIlllIlI[IlIllllIIlII]):
      IIlIIllIlII[lllIIIlIlllIlIlII+IlIllllIIlII] = IIlIIllIIIIlIl[lllIIIlIlllIlIlII]      
      lllIIIlIlllIlIlII += 1
    else:
      IIlIIllIlII[lllIIIlIlllIlIlII+IlIllllIIlII] = IllIIIlllllIlllIlI[IlIllllIIlII]      
      IlIllllIIlII += 1
def IllIllll(IIlIIllIlII):
  lllIlIllIIIIlIIll = len(IIlIIllIlII)
  if lllIlIllIIIIlIIll < 2:
    return                
  lIlIIllIIIllIllIl = lllIlIllIIIIlIIll // 2
  IIlIIllIIIIlIl = IIlIIllIlII[0:lIlIIllIIIllIllIl]           
  IllIIIlllllIlllIlI = IIlIIllIlII[lIlIIllIIIllIllIl:lllIlIllIIIIlIIll]           
  IllIllll(IIlIIllIIIIlIl)          
  IllIllll(IllIIIlllllIlllIlI)          
  IllIlllllllIllll(IIlIIllIIIIlIl, IllIIIlllllIlllIlI, IIlIIllIlII)        