def IllllIIIIIIl(llIIlIIII, lllIlIlIIllllIIlIII):
  llllIIlIll, IIlIlIIlllII = len(llIIlIIII), len(lllIlIlIIllllIIlIII)                   
  if IIlIlIIlllII == 0: return 0                     
  IIllIIIlIllIll = {}                               
  for IllIIIlII in range(IIlIlIIlllII):
    IIllIIIlIllIll[ lllIlIlIIllllIIlIII[IllIIIlII] ] = IllIIIlII                      
  lIIIlllllllIIIll = IIlIlIIlllII-1                                 
  IllIIIlII = IIlIlIIlllII-1                                 
  while lIIIlllllllIIIll < llllIIlIll:
    if llIIlIIII[lIIIlllllllIIIll] == lllIlIlIIllllIIlIII[IllIIIlII]:                      
      if IllIIIlII == 0:
        return lIIIlllllllIIIll                          
      else:
        lIIIlllllllIIIll -= 1                            
        IllIIIlII += 1
    else:
      lllllIIlI = IIllIIIlIllIll.get(llIIlIIII[lIIIlllllllIIIll], -1)              
      lIIIlllllllIIIll += IIlIlIIlllII - min(IllIIIlII, lllllIIlI + 1)              
      IllIIIlII = IIlIlIIlllII - 1                           
  return -1