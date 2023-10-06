def lIlIlIIllIllllIIllI(IlIlIIlIlIlIlIIIII, llIIIlllll, lIIlIIIllII):
  IIIllllllIIIlIlIIlIl = IlllllIlI = 0
  while IIIllllllIIIlIlIIlIl + IlllllIlI < len(lIIlIIIllII):
    if IlllllIlI == len(llIIIlllll) or (IIIllllllIIIlIlIIlIl < len(IlIlIIlIlIlIlIIIII) and IlIlIIlIlIlIlIIIII[IIIllllllIIIlIlIIlIl] < llIIIlllll[IlllllIlI]):
      lIIlIIIllII[IIIllllllIIIlIlIIlIl+IlllllIlI] = IlIlIIlIlIlIlIIIII[IIIllllllIIIlIlIIlIl]      
      IIIllllllIIIlIlIIlIl += 1
    else:
      lIIlIIIllII[IIIllllllIIIlIlIIlIl+IlllllIlI] = llIIIlllll[IlllllIlI]      
      IlllllIlI += 1
def lllIlIIIlllI(lIIlIIIllII):
  IIIlIllIl = len(lIIlIIIllII)
  if IIIlIllIl < 2:
    return                
  IIIlIIIIIlIIl = IIIlIllIl // 2
  IlIlIIlIlIlIlIIIII = lIIlIIIllII[0:]
  llIIIlllll = lIIlIIIllII[IIIlIIIIIlIIl:IIIlIllIl]           
  lllIlIIIlllI(IlIlIIlIlIlIlIIIII)          
  lllIlIIIlllI(llIIIlllll)          
  lIlIlIIllIllllIIllI(IlIlIIlIlIlIlIIIII, llIIIlllll, lIIlIIIllII)        