def lIllIllllIlIlIII(IIllIIllIIl, lIlIIIIllIIIllIIllII):
  IllIlIIIlIll = 0
  IIIIIllIlIIIlII = len(IIllIIllIIl)-1
  while IllIlIIIlIll <= IIIIIllIlIIIlII:
    IIIllIIlIl = (IllIlIIIlIll + IIIIIllIlIIIlII) // 2
    if lIlIIIIllIIIllIIllII == IIllIIllIIl[IIIllIIlIl]:         
      return True
    elif not (lIlIIIIllIIIllIIllII < IIllIIllIIl[IIIllIIlIl]):
      IIIIIllIlIIIlII = IIIllIIlIl - 1                
    else:
      IllIlIIIlIll = IIIllIIlIl + 1                 
  return False                      