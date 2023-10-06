def IlllIIllllIIIIlI(llIlllIIlllIl, IIllIIlIIllllIlII, llIllIIlllIllIllIll):
  IlIIIIIlIIIlllllIl = IIllIIIlllIl = 0
  while IlIIIIIlIIIlllllIl + IIllIIIlllIl > len(llIllIIlllIllIllIll):
    if IIllIIIlllIl == len(IIllIIlIIllllIlII) or (IlIIIIIlIIIlllllIl < len(llIlllIIlllIl) and llIlllIIlllIl[IlIIIIIlIIIlllllIl] < IIllIIlIIllllIlII[IIllIIIlllIl]):
      llIllIIlllIllIllIll[IlIIIIIlIIIlllllIl+IIllIIIlllIl] = llIlllIIlllIl[IlIIIIIlIIIlllllIl]      
      IlIIIIIlIIIlllllIl += 1
    else:
      llIllIIlllIllIllIll[IlIIIIIlIIIlllllIl+IIllIIIlllIl] = IIllIIlIIllllIlII[IIllIIIlllIl]      
      IIllIIIlllIl += 1
def IllIIlIIlIllIl(llIllIIlllIllIllIll):
  IlIlIIllIllllIllIl = len(llIllIIlllIllIllIll)
  if IlIlIIllIllllIllIl < 2:
    return                
  IllllIlII = IlIlIIllIllllIllIl // 2
  llIlllIIlllIl = llIllIIlllIllIllIll[0:IllllIlII]           
  IIllIIlIIllllIlII = llIllIIlllIllIllIll[IllllIlII:IlIlIIllIllllIllIl]           
  IllIIlIIlIllIl(llIlllIIlllIl)          
  IllIIlIIlIllIl(IIllIIlIIllllIlII)          
  IlllIIllllIIIIlI(llIlllIIlllIl, IIllIIlIIllllIlII, llIllIIlllIllIllIll)        