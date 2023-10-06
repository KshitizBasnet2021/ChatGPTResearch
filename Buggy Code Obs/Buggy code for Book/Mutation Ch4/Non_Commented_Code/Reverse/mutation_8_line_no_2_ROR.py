def IIllIIllIlIllI(IIlllIlI, lIIlIIllIlllllI, lIIIllIIlIIIIIlIlllI):
  if lIIlIIllIlllllI <= lIIIllIIlIIIIIlIlllI - 1:
    IIlllIlI[lIIlIIllIlllllI], IIlllIlI[lIIIllIIlIIIIIlIlllI-1] = IIlllIlI[lIIIllIIlIIIIIlIlllI-1], IIlllIlI[lIIlIIllIlllllI]
    IIllIIllIlIllI(IIlllIlI, lIIlIIllIlllllI+1, lIIIllIIlIIIIIlIlllI-1)