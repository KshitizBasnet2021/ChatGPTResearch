def IIIllIlIIlI(IlIlIIIllIlIIIIl, lllIIlIlIIIlIlllII, IIIIIIIIIII):
  lIIlIllII = lllllIIIIll = 0
  while lIIlIllII + lllllIIIIll < len(IIIIIIIIIII):
    if lllllIIIIll == len(lllIIlIlIIIlIlllII) or (lIIlIllII < len(IlIlIIIllIlIIIIl) and IlIlIIIllIlIIIIl[lIIlIllII] < lllIIlIlIIIlIlllII[lllllIIIIll]):
      IIIIIIIIIII[lIIlIllII+lllllIIIIll] = IlIlIIIllIlIIIIl[lIIlIllII]      
      lIIlIllII += 1
    else:
      IIIIIIIIIII[lIIlIllII - lllllIIIIll] = lllIIlIlIIIlIlllII[lllllIIIIll]
      lllllIIIIll += 1
def llIIllIlI(IIIIIIIIIII):
  llIlIIlIl = len(IIIIIIIIIII)
  if llIlIIlIl < 2:
    return                
  lIIIIIlIllII = llIlIIlIl // 2
  IlIlIIIllIlIIIIl = IIIIIIIIIII[0:lIIIIIlIllII]           
  lllIIlIlIIIlIlllII = IIIIIIIIIII[lIIIIIlIllII:llIlIIlIl]           
  llIIllIlI(IlIlIIIllIlIIIIl)          
  llIIllIlI(lllIIlIlIIIlIlllII)          
  IIIllIlIIlI(IlIlIIIllIlIIIIl, lllIIlIlIIIlIlllII, IIIIIIIIIII)        