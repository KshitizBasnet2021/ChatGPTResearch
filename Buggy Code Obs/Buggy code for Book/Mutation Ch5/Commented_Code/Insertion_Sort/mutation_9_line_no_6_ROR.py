def IIllIllIlIIllllIII(lIlIIIlIIllIIlIll):
  for IIllllIlIII in range(1, len(lIlIIIlIIllIIlIll)):         
    IllIIIlllIIll = lIlIIIlIIllIIlIll[IIllllIlIII]                       
    IlIIllIIllI = IIllllIlIII                            
    while (IlIIllIIllI > 0 and lIlIIIlIIllIIlIll[IlIIllIIllI - 1] >= IllIIIlllIIll):
      lIlIIIlIIllIIlIll[IlIIllIIllI] = lIlIIIlIIllIIlIll[IlIIllIIllI-1]
      IlIIllIIllI -= 1
    lIlIIIlIIllIIlIll[IlIIllIIllI] = IllIIIlllIIll                       