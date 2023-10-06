def lIllIlll(IIIIllllIllllllIIIII, IIlIlIllllll):
  lIllIllIII = 0
  lllIlIIll = len(IIIIllllIllllllIIIII)-1
  while lIllIllIII < lllIlIIll:
    IllIIlIlIIIlIllIll = (lIllIllIII + lllIlIIll) // 2
    if IIlIlIllllll == IIIIllllIllllllIIIII[IllIIlIlIIIlIllIll]:         
      return True
    elif IIlIlIllllll < IIIIllllIllllllIIIII[IllIIlIlIIIlIllIll]:
      lllIlIIll = IllIIlIlIIIlIllIll - 1                
    else:
      lIllIllIII = IllIIlIlIIIlIllIll + 1                 
  return False                      