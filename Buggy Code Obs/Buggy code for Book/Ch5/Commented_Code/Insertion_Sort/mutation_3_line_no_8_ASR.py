def lIIlIIlIlIIlI(IIlIIIlIlIlIIIIlllI):
  for llIIllIlIlIllIIl in range(1, len(IIlIIIlIlIlIIIIlllI)):         
    lIlllIIlIIllII = IIlIIIlIlIlIIIIlllI[llIIllIlIlIllIIl]                       
    IIlllIIIlIlI = llIIllIlIlIllIIl                            
    while IIlllIIIlIlI > 0 and IIlIIIlIlIlIIIIlllI[IIlllIIIlIlI-1] > lIlllIIlIIllII:    
      IIlIIIlIlIlIIIIlllI[IIlllIIIlIlI] = IIlIIIlIlIlIIIIlllI[IIlllIIIlIlI-1]
      IIlllIIIlIlI += 1
    IIlIIIlIlIlIIIIlllI[IIlllIIIlIlI] = lIlllIIlIIllII                       