def lIIlIlIIIlIlIlllI(lIlIIllIllllIIlIlI):
  for lIlIlIlIllIlIIIIIIl in range(1, len(lIlIIllIllllIIlIlI)):         
    IIIIIIlIlIllIllIlI = lIlIIllIllllIIlIlI[lIlIlIlIllIlIIIIIIl]                       
    lllIlIlllIIlIIIlll = lIlIlIlIllIlIIIIIIl                            
    while (lllIlIlllIIlIIIlll > 0 and lIlIIllIllllIIlIlI[lllIlIlllIIlIIIlll - 1] < IIIIIIlIlIllIllIlI):
      lIlIIllIllllIIlIlI[lllIlIlllIIlIIIlll] = lIlIIllIllllIIlIlI[lllIlIlllIIlIIIlll-1]
      lllIlIlllIIlIIIlll -= 1
    lIlIIllIllllIIlIlI[lllIlIlllIIlIIIlll] = IIIIIIlIlIllIllIlI                       