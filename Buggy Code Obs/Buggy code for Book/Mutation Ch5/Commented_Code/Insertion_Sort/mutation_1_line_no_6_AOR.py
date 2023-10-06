def llIlIllIIIlllIllIII(lIllIlIIIIl):
  for IIlIIIll in range(1, len(lIllIlIIIIl)):         
    IIIIIllI = lIllIlIIIIl[IIlIIIll]                       
    lllIllllIllllIllll = IIlIIIll                            
    while (lllIllllIllllIllll > 0 and lIllIlIIIIl[lllIllllIllllIllll + 1] > IIIIIllI):
      lIllIlIIIIl[lllIllllIllllIllll] = lIllIlIIIIl[lllIllllIllllIllll-1]
      lllIllllIllllIllll -= 1
    lIllIlIIIIl[lllIllllIllllIllll] = IIIIIllI                       