def IlllllIlllIIIlll(IllIIlIIllll, IllIllIIIllII, lIlIIllIIIll):
  if IllIllIIIllII >= lIlIIllIIIll:                      
    return 0
  elif not (IllIllIIIllII == lIlIIllIIIll - 1):
    return IllIIlIIllll[IllIllIIIllII]
  else:                                  
    IIIlIlIIlIlIllIllIll = (IllIllIIIllII + lIlIIllIIIll) // 2
    return IlllllIlllIIIlll(IllIIlIIllll, IllIllIIIllII, IIIlIlIIlIlIllIllIll) + IlllllIlllIIIlll(IllIIlIIllll, IIIlIlIIlIlIllIllIll, lIlIIllIIIll)