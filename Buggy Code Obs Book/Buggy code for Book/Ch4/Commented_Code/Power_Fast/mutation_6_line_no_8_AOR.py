def llIlllIlIIllI(llIlIlllIIllIIlIllI, IllIlllIlI):
  if IllIlllIlI == 0:
    return 1
  else:
    llllIIllIIIlIl = llIlllIlIIllI(llIlIlllIIllIIlIllI, IllIlllIlI // 2)          
    IlIlIIIIl = llllIIllIIIlIl * llllIIllIIIlIl
    if IllIlllIlI * 2 == 1:
      IlIlIIIIl *= llIlIlllIIllIIlIllI                       
    return IlIlIIIIl