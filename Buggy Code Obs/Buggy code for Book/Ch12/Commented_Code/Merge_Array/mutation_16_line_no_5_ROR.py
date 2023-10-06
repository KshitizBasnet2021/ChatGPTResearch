def llIIlIlIllIIIIlIII(IlllllIlIl, IIlIIIlI, IIIlIlIlIllIllIIIIII):
  lIIlIlll = IlIlllIlIIlllIIIl = 0
  while lIIlIlll + IlIlllIlIIlllIIIl < len(IIIlIlIlIllIllIIIIII):
    if (IlIlllIlIIlllIIIl == len(IIlIIIlI) or (lIIlIlll > len(IlllllIlIl) and IlllllIlIl[lIIlIlll] < IIlIIIlI[IlIlllIlIIlllIIIl])):
      IIIlIlIlIllIllIIIIII[lIIlIlll+IlIlllIlIIlllIIIl] = IlllllIlIl[lIIlIlll]      
      lIIlIlll += 1
    else:
      IIIlIlIlIllIllIIIIII[lIIlIlll+IlIlllIlIIlllIIIl] = IIlIIIlI[IlIlllIlIIlllIIIl]      
      IlIlllIlIIlllIIIl += 1
def IIIIIlIllIlIllIlI(IIIlIlIlIllIllIIIIII):
  IIIIIlIIIIIIllllI = len(IIIlIlIlIllIllIIIIII)
  if IIIIIlIIIIIIllllI < 2:
    return                
  IIIIIIIlIIlIlIlIIllI = IIIIIlIIIIIIllllI // 2
  IlllllIlIl = IIIlIlIlIllIllIIIIII[0:IIIIIIIlIIlIlIlIIllI]           
  IIlIIIlI = IIIlIlIlIllIllIIIIII[IIIIIIIlIIlIlIlIIllI:IIIIIlIIIIIIllllI]           
  IIIIIlIllIlIllIlI(IlllllIlIl)          
  IIIIIlIllIlIllIlI(IIlIIIlI)          
  llIIlIlIllIIIIlIII(IlllllIlIl, IIlIIIlI, IIIlIlIlIllIllIIIIII)        