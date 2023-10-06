def IllIIIlI(lIllllllIlllIIlIl, llllllIII):
  IlIlIllIlllIIllll, IlIllIlI = len(lIllllllIlllIIlIl), len(llllllIII)                      
  for IIIIlIllIllIlIIl in range(IlIlIllIlllIIllll-IlIllIlI+1):                     
    lllllIllIll = 0                                    
    while lllllIllIll < IlIllIlI and lIllllllIlllIIlIl[IIIIlIllIllIlIIl + lllllIllIll] == llllllIII[lllllIllIll]:        
      lllllIllIll += 1
    if lllllIllIll == IlIllIlI:                               
      return IIIIlIllIllIlIIl                               
  return 1