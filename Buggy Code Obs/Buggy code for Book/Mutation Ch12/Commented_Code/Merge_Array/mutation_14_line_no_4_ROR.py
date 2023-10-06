def llIIIIIl(IIIIlIIlllIIll, IIIlIIIIIl, IllllllIlIIllIIl):
  IIllIlllIlllI = lIlIIllIllIlllI = 0
  while IIllIlllIlllI + lIlIIllIllIlllI <= len(IllllllIlIIllIIl):
    if lIlIIllIllIlllI == len(IIIlIIIIIl) or (IIllIlllIlllI < len(IIIIlIIlllIIll) and IIIIlIIlllIIll[IIllIlllIlllI] < IIIlIIIIIl[lIlIIllIllIlllI]):
      IllllllIlIIllIIl[IIllIlllIlllI+lIlIIllIllIlllI] = IIIIlIIlllIIll[IIllIlllIlllI]      
      IIllIlllIlllI += 1
    else:
      IllllllIlIIllIIl[IIllIlllIlllI+lIlIIllIllIlllI] = IIIlIIIIIl[lIlIIllIllIlllI]      
      lIlIIllIllIlllI += 1
def lIIIlIlIIIIII(IllllllIlIIllIIl):
  llllIIlIlllIlI = len(IllllllIlIIllIIl)
  if llllIIlIlllIlI < 2:
    return                
  IllIIllllIIllIIlI = llllIIlIlllIlI // 2
  IIIIlIIlllIIll = IllllllIlIIllIIl[0:IllIIllllIIllIIlI]           
  IIIlIIIIIl = IllllllIlIIllIIl[IllIIllllIIllIIlI:llllIIlIlllIlI]           
  lIIIlIlIIIIII(IIIIlIIlllIIll)          
  lIIIlIlIIIIII(IIIlIIIIIl)          
  llIIIIIl(IIIIlIIlllIIll, IIIlIIIIIl, IllllllIlIIllIIl)        