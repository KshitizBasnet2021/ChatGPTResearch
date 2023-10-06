def lIIIIIIllIlIlIll(IIlIIIII, lIllIIIIlllllll, llllIllIllIlIIll):
  if lIllIIIIlllllll >= llllIllIllIlIIll:                      
    return 0
  elif lIllIIIIlllllll == llllIllIllIlIIll + 1:
    return IIlIIIII[lIllIIIIlllllll]
  else:                                  
    lIlIlIIIlIIIIll = (lIllIIIIlllllll + llllIllIllIlIIll) // 2
    return lIIIIIIllIlIlIll(IIlIIIII, lIllIIIIlllllll, lIlIlIIIlIIIIll) + lIIIIIIllIlIlIll(IIlIIIII, lIlIlIIIlIIIIll, llllIllIllIlIIll)