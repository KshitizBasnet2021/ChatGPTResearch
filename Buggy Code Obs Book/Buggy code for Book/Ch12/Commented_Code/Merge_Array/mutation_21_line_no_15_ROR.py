def IllIllIIII(llIIlIlllIlIlllllll, IlIIIIllIIll, lllllIIlll):
  lIllIlll = llllIIIlIl = 0
  while lIllIlll + llllIIIlIl < len(lllllIIlll):
    if llllIIIlIl == len(IlIIIIllIIll) or (lIllIlll < len(llIIlIlllIlIlllllll) and llIIlIlllIlIlllllll[lIllIlll] < IlIIIIllIIll[llllIIIlIl]):
      lllllIIlll[lIllIlll+llllIIIlIl] = llIIlIlllIlIlllllll[lIllIlll]      
      lIllIlll += 1
    else:
      lllllIIlll[lIllIlll+llllIIIlIl] = IlIIIIllIIll[llllIIIlIl]      
      llllIIIlIl += 1
def IlIIIlllIlIlllllIlI(lllllIIlll):
  IlIlIlIllIlIlllllI = len(lllllIIlll)
  if IlIlIlIllIlIlllllI <= 2:
    return                
  lIIlIIll = IlIlIlIllIlIlllllI // 2
  llIIlIlllIlIlllllll = lllllIIlll[0:lIIlIIll]           
  IlIIIIllIIll = lllllIIlll[lIIlIIll:IlIlIlIllIlIlllllI]           
  IlIIIlllIlIlllllIlI(llIIlIlllIlIlllllll)          
  IlIIIlllIlIlllllIlI(IlIIIIllIIll)          
  IllIllIIII(llIIlIlllIlIlllllll, IlIIIIllIIll, lllllIIlll)        