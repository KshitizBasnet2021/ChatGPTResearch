def lllIIllI(IlIlIlIlIlIlIl, lIllIllIllIII, IIlllIlllllIIll):
  lIIIIlIlllllIIIl = IIllIIllIIIlIlIll = 0
  while lIIIIlIlllllIIIl + IIllIIllIIIlIlIll < len(IIlllIlllllIIll):
    if IIllIIllIIIlIlIll == len(lIllIllIllIII) or (lIIIIlIlllllIIIl < len(IlIlIlIlIlIlIl) and IlIlIlIlIlIlIl[lIIIIlIlllllIIIl] < lIllIllIllIII[IIllIIllIIIlIlIll]):
      IIlllIlllllIIll[lIIIIlIlllllIIIl+IIllIIllIIIlIlIll] = IlIlIlIlIlIlIl[lIIIIlIlllllIIIl]      
      lIIIIlIlllllIIIl -= 1
    else:
      IIlllIlllllIIll[lIIIIlIlllllIIIl+IIllIIllIIIlIlIll] = lIllIllIllIII[IIllIIllIIIlIlIll]      
      IIllIIllIIIlIlIll += 1
def llIlIIllI(IIlllIlllllIIll):
  IlIlIIIIllIlIlIlIIl = len(IIlllIlllllIIll)
  if IlIlIIIIllIlIlIlIIl < 2:
    return                
  llIIllIllIlIlll = IlIlIIIIllIlIlIlIIl // 2
  IlIlIlIlIlIlIl = IIlllIlllllIIll[0:llIIllIllIlIlll]           
  lIllIllIllIII = IIlllIlllllIIll[llIIllIllIlIlll:IlIlIIIIllIlIlIlIIl]           
  llIlIIllI(IlIlIlIlIlIlIl)          
  llIlIIllI(lIllIllIllIII)          
  lllIIllI(IlIlIlIlIlIlIl, lIllIllIllIII, IIlllIlllllIIll)        