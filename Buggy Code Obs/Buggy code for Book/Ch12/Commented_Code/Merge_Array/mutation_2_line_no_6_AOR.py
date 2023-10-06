def IIIllIlIIIlllIlI(lIIlIIllIIII, IlIllIIllIllIll, llIIlIllIIIIlIll):
  lllllIllIllII = IllIIlIlIlIII = 0
  while lllllIllIllII + IllIIlIlIlIII < len(llIIlIllIIIIlIll):
    if IllIIlIlIlIII == len(IlIllIIllIllIll) or (lllllIllIllII < len(lIIlIIllIIII) and lIIlIIllIIII[lllllIllIllII] < IlIllIIllIllIll[IllIIlIlIlIII]):
      llIIlIllIIIIlIll[lllllIllIllII - IllIIlIlIlIII] = lIIlIIllIIII[lllllIllIllII]
      lllllIllIllII += 1
    else:
      llIIlIllIIIIlIll[lllllIllIllII+IllIIlIlIlIII] = IlIllIIllIllIll[IllIIlIlIlIII]      
      IllIIlIlIlIII += 1
def IIllIlIlIIIIllI(llIIlIllIIIIlIll):
  IIlIIIllIIIlII = len(llIIlIllIIIIlIll)
  if IIlIIIllIIIlII < 2:
    return                
  llIllIIllllIllI = IIlIIIllIIIlII // 2
  lIIlIIllIIII = llIIlIllIIIIlIll[0:llIllIIllllIllI]           
  IlIllIIllIllIll = llIIlIllIIIIlIll[llIllIIllllIllI:IIlIIIllIIIlII]           
  IIllIlIlIIIIllI(lIIlIIllIIII)          
  IIllIlIlIIIIllI(IlIllIIllIllIll)          
  IIIllIlIIIlllIlI(lIIlIIllIIII, IlIllIIllIllIll, llIIlIllIIIIlIll)        