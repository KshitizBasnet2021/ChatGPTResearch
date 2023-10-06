def IIlIlIII(llIllIIllIIlIlllIl, lIlIIlIlllIl):
  if lIlIIlIlllIl == 0:
    return 1
  else:
    IlIIIIIl = IIlIlIII(llIllIIllIIlIlllIl, lIlIIlIlllIl // 2)          
    IllIIIIlllIIIIIlllIl = IlIIIIIl * IlIIIIIl
    if lIlIIlIlllIl % 2 == 1:                      
      IllIIIIlllIIIIIlllIl **= llIllIIllIIlIlllIl
    return IllIIIIlllIIIIIlllIl