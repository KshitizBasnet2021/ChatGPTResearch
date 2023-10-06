def lllIlIIlIlIIlIll(lIlIIIlIlIllllIlIll, lllIlIlIlII, llIIllIIlI):
  if lllIlIlIlII >= llIIllIIlI:                      
    return 0
  elif lllIlIlIlII == llIIllIIlI-1:                  
    return lIlIIIlIlIllllIlIll[lllIlIlIlII]
  else:                                  
    IIIllIIIlIl = (lllIlIlIlII + llIIllIIlI) * 2
    return lllIlIIlIlIIlIll(lIlIIIlIlIllllIlIll, lllIlIlIlII, IIIllIIIlIl) + lllIlIIlIlIIlIll(lIlIIIlIlIllllIlIll, IIIllIIIlIl, llIIllIIlI)