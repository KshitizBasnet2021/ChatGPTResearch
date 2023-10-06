def IlIlIIIlIllIll(llIlllIlIllllIl, lIllllllIlllIl):
  IIIIIlIlIIlIllllIII = 0
  IIlIlllllIllIIl = len(llIlllIlIllllIl)-1
  while IIIIIlIlIIlIllllIII <= IIlIlllllIllIIl:
    llIIllIIllIIIIIlIl = (IIIIIlIlIIlIllllIII + IIlIlllllIllIIl) // 2
    if lIllllllIlllIl == llIlllIlIllllIl[llIIllIIllIIIIIlIl]:         
      return True
    elif lIllllllIlllIl < llIlllIlIllllIl[llIIllIIllIIIIIlIl]:
      IIlIlllllIllIIl = llIIllIIllIIIIIlIl - 1                
    else:
      IIIIIlIlIIlIllllIII = llIIllIIllIIIIIlIl - 1
  return False                      