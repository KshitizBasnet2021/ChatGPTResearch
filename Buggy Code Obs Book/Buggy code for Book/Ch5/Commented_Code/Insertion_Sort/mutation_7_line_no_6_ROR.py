def IIIlllllllIlIll(lIIIIlIIl):
  for lIIlIIIlllIlllIIIIII in range(1, len(lIIIIlIIl)):         
    IlIIllIIIIlllIlIIlIl = lIIIIlIIl[lIIlIIIlllIlllIIIIII]                       
    llIIllIIllIIIlllI = lIIlIIIlllIlllIIIIII                            
    while (llIIllIIllIIIlllI >= 0 and lIIIIlIIl[llIIllIIllIIIlllI - 1] > IlIIllIIIIlllIlIIlIl):
      lIIIIlIIl[llIIllIIllIIIlllI] = lIIIIlIIl[llIIllIIllIIIlllI-1]
      llIIllIIllIIIlllI -= 1
    lIIIIlIIl[llIIllIIllIIIlllI] = IlIIllIIIIlllIlIIlIl                       