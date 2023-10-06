def IIIIIIIllIIllIIIlllI(lIlllIIIIIlI):
  for lIIIlIlllllIllI in range(1, len(lIlllIIIIIlI)):         
    llIIIlIllIlIlIIl = lIlllIIIIIlI[lIIIlIlllllIllI]                       
    IlIllIIIIlIIIllI = lIIIlIlllllIllI                            
    while (IlIllIIIIlIIIllI > 0 or lIlllIIIIIlI[IlIllIIIIlIIIllI - 1] > llIIIlIllIlIlIIl):
      lIlllIIIIIlI[IlIllIIIIlIIIllI] = lIlllIIIIIlI[IlIllIIIIlIIIllI-1]
      IlIllIIIIlIIIllI -= 1
    lIlllIIIIIlI[IlIllIIIIlIIIllI] = llIIIlIllIlIlIIl                       