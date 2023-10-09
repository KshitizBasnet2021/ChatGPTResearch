def lIIllIIlIIlI(lIIIIIlllIlIlllIlII, llIIIIllll, llIIlIllIllllIllllll):
  IIllIlIlIlIIIIl = IIlllIIIlIIllII = 0
  while IIllIlIlIlIIIIl + IIlllIIIlIIllII < len(llIIlIllIllllIllllll):
    if (IIlllIIIlIIllII == len(llIIIIllll) or (IIllIlIlIlIIIIl <= len(lIIIIIlllIlIlllIlII) and lIIIIIlllIlIlllIlII[IIllIlIlIlIIIIl] < llIIIIllll[IIlllIIIlIIllII])):
      llIIlIllIllllIllllll[IIllIlIlIlIIIIl+IIlllIIIlIIllII] = lIIIIIlllIlIlllIlII[IIllIlIlIlIIIIl]      
      IIllIlIlIlIIIIl += 1
    else:
      llIIlIllIllllIllllll[IIllIlIlIlIIIIl+IIlllIIIlIIllII] = llIIIIllll[IIlllIIIlIIllII]      
      IIlllIIIlIIllII += 1
def IlIIllIlIllIlll(llIIlIllIllllIllllll):
  lIllIlIlIIIIlIl = len(llIIlIllIllllIllllll)
  if lIllIlIlIIIIlIl < 2:
    return                
  lllIIlIIl = lIllIlIlIIIIlIl // 2
  lIIIIIlllIlIlllIlII = llIIlIllIllllIllllll[0:lllIIlIIl]           
  llIIIIllll = llIIlIllIllllIllllll[lllIIlIIl:lIllIlIlIIIIlIl]           
  IlIIllIlIllIlll(lIIIIIlllIlIlllIlII)          
  IlIIllIlIllIlll(llIIIIllll)          
  lIIllIIlIIlI(lIIIIIlllIlIlllIlII, llIIIIllll, llIIlIllIllllIllllll)        