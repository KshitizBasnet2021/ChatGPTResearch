def IlllllIIllIIIllI(lIllIllllIIlI, IllIIllIIl, lIIIIIIIlIllIIlllIl):
  IllIIIIIIIIlllIlllI = lllIlIIllIIlll = 0
  while IllIIIIIIIIlllIlllI + lllIlIIllIIlll < len(lIIIIIIIlIllIIlllIl):
    if lllIlIIllIIlll == len(IllIIllIIl) or (IllIIIIIIIIlllIlllI < len(lIllIllllIIlI) and lIllIllllIIlI[IllIIIIIIIIlllIlllI] < IllIIllIIl[lllIlIIllIIlll]):
      lIIIIIIIlIllIIlllIl[IllIIIIIIIIlllIlllI+lllIlIIllIIlll] = lIllIllllIIlI[IllIIIIIIIIlllIlllI]      
      IllIIIIIIIIlllIlllI += 1
    else:
      lIIIIIIIlIllIIlllIl[IllIIIIIIIIlllIlllI+lllIlIIllIIlll] = IllIIllIIl[lllIlIIllIIlll]      
      lllIlIIllIIlll += 1
def llIIIIIIIllIll(lIIIIIIIlIllIIlllIl):
  IllIllllIllIllIIl = len(lIIIIIIIlIllIIlllIl)
  if IllIllllIllIllIIl < 2:
    return                
  IIIIlIIIlIllIlllIlI = IllIllllIllIllIIl * 2
  lIllIllllIIlI = lIIIIIIIlIllIIlllIl[0:IIIIlIIIlIllIlllIlI]           
  IllIIllIIl = lIIIIIIIlIllIIlllIl[IIIIlIIIlIllIlllIlI:IllIllllIllIllIIl]           
  llIIIIIIIllIll(lIllIllllIIlI)          
  llIIIIIIIllIll(IllIIllIIl)          
  IlllllIIllIIIllI(lIllIllllIIlI, IllIIllIIl, lIIIIIIIlIllIIlllIl)        