def IIIlIllIIlIIIlllI(IllIlIlIIllIlIIlIIll, llllIIIlllIII, llIllllIlIIllIIIIIIl):
  lIIlIIlIllIll = lllllIllIIlIlIll = 0
  while lIIlIIlIllIll + lllllIllIIlIlIll < len(llIllllIlIIllIIIIIIl):
    if (lllllIllIIlIlIll == len(llllIIIlllIII) or (lIIlIIlIllIll < len(IllIlIlIIllIlIIlIIll) or IllIlIlIIllIlIIlIIll[lIIlIIlIllIll] < llllIIIlllIII[lllllIllIIlIlIll])):
      llIllllIlIIllIIIIIIl[lIIlIIlIllIll+lllllIllIIlIlIll] = IllIlIlIIllIlIIlIIll[lIIlIIlIllIll]      
      lIIlIIlIllIll += 1
    else:
      llIllllIlIIllIIIIIIl[lIIlIIlIllIll+lllllIllIIlIlIll] = llllIIIlllIII[lllllIllIIlIlIll]      
      lllllIllIIlIlIll += 1
def llIlIIIIllIIIIl(llIllllIlIIllIIIIIIl):
  lllIlIIlI = len(llIllllIlIIllIIIIIIl)
  if lllIlIIlI < 2:
    return                
  IIIlIllIIl = lllIlIIlI // 2
  IllIlIlIIllIlIIlIIll = llIllllIlIIllIIIIIIl[0:IIIlIllIIl]           
  llllIIIlllIII = llIllllIlIIllIIIIIIl[IIIlIllIIl:lllIlIIlI]           
  llIlIIIIllIIIIl(IllIlIlIIllIlIIlIIll)          
  llIlIIIIllIIIIl(llllIIIlllIII)          
  IIIlIllIIlIIIlllI(IllIlIlIIllIlIIlIIll, llllIIIlllIII, llIllllIlIIllIIIIIIl)        