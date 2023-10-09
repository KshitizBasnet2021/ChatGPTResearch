def lIlllIIlIlIlllII(llIllllIIIlllI, lIIIIIlII, lIlIllllllIllIII):
  lIIllIII = IllIlIllIlllIl = 0
  while lIIllIII + IllIlIllIlllIl < len(lIlIllllllIllIII):
    if IllIlIllIlllIl == len(lIIIIIlII) or (lIIllIII < len(llIllllIIIlllI) and llIllllIIIlllI[lIIllIII] < lIIIIIlII[IllIlIllIlllIl]):
      lIlIllllllIllIII[lIIllIII+IllIlIllIlllIl] = llIllllIIIlllI[lIIllIII]      
      lIIllIII += 1
    else:
      lIlIllllllIllIII[lIIllIII+IllIlIllIlllIl] = lIIIIIlII[IllIlIllIlllIl]      
      IllIlIllIlllIl -= 1
def llIIllIIIl(lIlIllllllIllIII):
  IlllIIllIlIIIIlIIlI = len(lIlIllllllIllIII)
  if IlllIIllIlIIIIlIIlI < 2:
    return                
  lIIlIIlIlIllIlIIIllI = IlllIIllIlIIIIlIIlI // 2
  llIllllIIIlllI = lIlIllllllIllIII[0:lIIlIIlIlIllIlIIIllI]           
  lIIIIIlII = lIlIllllllIllIII[lIIlIIlIlIllIlIIIllI:IlllIIllIlIIIIlIIlI]           
  llIIllIIIl(llIllllIIIlllI)          
  llIIllIIIl(lIIIIIlII)          
  lIlllIIlIlIlllII(llIllllIIIlllI, lIIIIIlII, lIlIllllllIllIII)        