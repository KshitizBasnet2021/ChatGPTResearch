def IllIIIllll(IIlIlllIllllI):
  for IlllllIIlIIII in range(1, len(IIlIlllIllllI)):         
    IlllIIlll = IIlIlllIllllI[IlllllIIlIIII]                       
    IIIllllIIIllIl = IlllllIIlIIII                            
    while not ((IIIllllIIIllIl > 0 and IIlIlllIllllI[IIIllllIIIllIl - 1] > IlllIIlll)):
      IIlIlllIllllI[IIIllllIIIllIl] = IIlIlllIllllI[IIIllllIIIllIl-1]
      IIIllllIIIllIl -= 1
    IIlIlllIllllI[IIIllllIIIllIl] = IlllIIlll                       