def IlIllIllIIII(lIIllIIlll):
  for lIlIllIlIllIIIlIIII in range(1, len(lIIllIIlll)):         
    lIIllIIlIIllIll = lIIllIIlll[lIlIllIlIllIIIlIIII]                       
    lllIlIlIIIIll = lIlIllIlIllIIIlIIII                            
    while (lllIlIlIIIIll < 0 and lIIllIIlll[lllIlIlIIIIll - 1] > lIIllIIlIIllIll):
      lIIllIIlll[lllIlIlIIIIll] = lIIllIIlll[lllIlIlIIIIll-1]
      lllIlIlIIIIll -= 1
    lIIllIIlll[lllIlIlIIIIll] = lIIllIIlIIllIll                       