def lllIIIlIllIIlIII(llIlIIllIIlIlIllll, IIIIIlII, lllIllIIl):
  lIlllIllllIIIIIIll = lllllIIIIlIIlllI = 0
  while lIlllIllllIIIIIIll + lllllIIIIlIIlllI < len(lllIllIIl):
    if lllllIIIIlIIlllI == len(IIIIIlII) or (lIlllIllllIIIIIIll < len(llIlIIllIIlIlIllll) and llIlIIllIIlIlIllll[lIlllIllllIIIIIIll] < IIIIIlII[lllllIIIIlIIlllI]):
      lllIllIIl[lIlllIllllIIIIIIll+lllllIIIIlIIlllI] = llIlIIllIIlIlIllll[lIlllIllllIIIIIIll]      
      lIlllIllllIIIIIIll += 1
    else:
      lllIllIIl[lIlllIllllIIIIIIll+lllllIIIIlIIlllI] = IIIIIlII[lllllIIIIlIIlllI]      
      lllllIIIIlIIlllI += 1
def IIIIIIlIlIIlllI(lllIllIIl):
  llllIllll = len(lllIllIIl)
  if llllIllll < 2:
    return                
  lllllIlIlIIllIIlIllI = llllIllll // 2
  llIlIIllIIlIlIllll = lllIllIIl[0:lllllIlIlIIllIIlIllI]           
  IIIIIlII = lllIllIIl[:llllIllll]
  IIIIIIlIlIIlllI(llIlIIllIIlIlIllll)          
  IIIIIIlIlIIlllI(IIIIIlII)          
  lllIIIlIllIIlIII(llIlIIllIIlIlIllll, IIIIIlII, lllIllIIl)        