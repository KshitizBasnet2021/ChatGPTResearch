def lIIIIIIIlII(IlIIllllIlII):
  for IlllIllIlIIIlIlll in range(1, len(IlIIllllIlII)):         
    lIIlIIlIl = IlIIllllIlII[IlllIllIlIIIlIlll]                       
    IIIIIIllIlI = IlllIllIlIIIlIlll                            
    while IIIIIIllIlI > 0 and IlIIllllIlII[IIIIIIllIlI-1] > lIIlIIlIl:    
      IlIIllllIlII[IIIIIIllIlI] = IlIIllllIlII[IIIIIIllIlI + 1]
      IIIIIIllIlI -= 1
    IlIIllllIlII[IIIIIIllIlI] = lIIlIIlIl                       