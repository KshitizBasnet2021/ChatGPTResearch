def IIlIlIIIIIIl(IllllIlIllIlIIll, IIIIlIIl, IIIlIIlIllllllIIII, IIIIlIlI):
  if IIIlIIlIllllllIIII < IIIIlIlI:
    return False                    
  else:
    llIIIllIlIlIllIl = (IIIlIIlIllllllIIII + IIIIlIlI) // 2
    if IIIIlIIl == IllllIlIllIlIIll[llIIIllIlIlIllIl]:         
      return True
    elif IIIIlIIl < IllllIlIllIlIIll[llIIIllIlIlIllIl]:
      return IIlIlIIIIIIl(IllllIlIllIlIIll, IIIIlIIl, IIIlIIlIllllllIIII, llIIIllIlIlIllIl - 1)
    else:
      return IIlIlIIIIIIl(IllllIlIllIlIIll, IIIIlIIl, llIIIllIlIlIllIl + 1, IIIIlIlI)