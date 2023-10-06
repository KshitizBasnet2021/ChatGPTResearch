def IlIIlllllIIllllllllI(IllllIIlIlIlIlIIIIl, lIlIlIlIIIIllIl, llIllIIIIl):
  lIllIIllllIIlIlIIlII = lIlllIll = 0
  while lIllIIllllIIlIlIIlII + lIlllIll < len(llIllIIIIl):
    if (lIlllIll == len(lIlIlIlIIIIllIl) or (lIllIIllllIIlIlIIlII < len(IllllIIlIlIlIlIIIIl) and IllllIIlIlIlIlIIIIl[lIllIIllllIIlIlIIlII] <= lIlIlIlIIIIllIl[lIlllIll])):
      llIllIIIIl[lIllIIllllIIlIlIIlII+lIlllIll] = IllllIIlIlIlIlIIIIl[lIllIIllllIIlIlIIlII]      
      lIllIIllllIIlIlIIlII += 1
    else:
      llIllIIIIl[lIllIIllllIIlIlIIlII+lIlllIll] = lIlIlIlIIIIllIl[lIlllIll]      
      lIlllIll += 1
def llIIIIllIIllIlllIll(llIllIIIIl):
  IlllIIllIllIIIlllll = len(llIllIIIIl)
  if IlllIIllIllIIIlllll < 2:
    return                
  IlIIlIIIlIIlllllIII = IlllIIllIllIIIlllll // 2
  IllllIIlIlIlIlIIIIl = llIllIIIIl[0:IlIIlIIIlIIlllllIII]           
  lIlIlIlIIIIllIl = llIllIIIIl[IlIIlIIIlIIlllllIII:IlllIIllIllIIIlllll]           
  llIIIIllIIllIlllIll(IllllIIlIlIlIlIIIIl)          
  llIIIIllIIllIlllIll(lIlIlIlIIIIllIl)          
  IlIIlllllIIllllllllI(IllllIIlIlIlIlIIIIl, lIlIlIlIIIIllIl, llIllIIIIl)        