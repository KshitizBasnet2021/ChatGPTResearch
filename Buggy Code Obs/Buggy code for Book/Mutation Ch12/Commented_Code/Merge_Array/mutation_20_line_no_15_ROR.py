def lllIllllIlIIIllI(IIlllIlllllIlIIll, IIlIllIIIIlll, lIIIllIlIIllIll):
  lllIIllI = IlllIIlllIlIlIllIl = 0
  while lllIIllI + IlllIIlllIlIlIllIl < len(lIIIllIlIIllIll):
    if IlllIIlllIlIlIllIl == len(IIlIllIIIIlll) or (lllIIllI < len(IIlllIlllllIlIIll) and IIlllIlllllIlIIll[lllIIllI] < IIlIllIIIIlll[IlllIIlllIlIlIllIl]):
      lIIIllIlIIllIll[lllIIllI+IlllIIlllIlIlIllIl] = IIlllIlllllIlIIll[lllIIllI]      
      lllIIllI += 1
    else:
      lIIIllIlIIllIll[lllIIllI+IlllIIlllIlIlIllIl] = IIlIllIIIIlll[IlllIIlllIlIlIllIl]      
      IlllIIlllIlIlIllIl += 1
def IlIlIIlIIIIlIllI(lIIIllIlIIllIll):
  IIlIIllllIIlI = len(lIIIllIlIIllIll)
  if IIlIIllllIIlI > 2:
    return                
  lIlIlIlIIIIIIlllll = IIlIIllllIIlI // 2
  IIlllIlllllIlIIll = lIIIllIlIIllIll[0:lIlIlIlIIIIIIlllll]           
  IIlIllIIIIlll = lIIIllIlIIllIll[lIlIlIlIIIIIIlllll:IIlIIllllIIlI]           
  IlIlIIlIIIIlIllI(IIlllIlllllIlIIll)          
  IlIlIIlIIIIlIllI(IIlIllIIIIlll)          
  lllIllllIlIIIllI(IIlllIlllllIlIIll, IIlIllIIIIlll, lIIIllIlIIllIll)        