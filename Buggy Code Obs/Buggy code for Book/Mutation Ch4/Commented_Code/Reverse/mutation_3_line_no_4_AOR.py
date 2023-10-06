def lIllIIIIlI(lIlllIllI, llIIlIlII, lIlIIIll):
  if llIIlIlII < lIlIIIll - 1:                         
    (lIlllIllI[llIIlIlII], lIlllIllI[lIlIIIll - 1]) = (lIlllIllI[lIlIIIll + 1], lIlllIllI[llIIlIlII])
    lIllIIIIlI(lIlllIllI, llIIlIlII+1, lIlIIIll-1)                