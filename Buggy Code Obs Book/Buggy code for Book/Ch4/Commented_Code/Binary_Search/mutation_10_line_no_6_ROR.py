def llIIIIIIlIlllII(llIlIlIIIlIllIlllI, lllllIIIllIlIllIIl, lllIIIlIlII, IIlIIIIll):
  if lllIIIlIlII >= IIlIIIIll:
    return False                    
  else:
    IIIlIllllIlllIII = (lllIIIlIlII + IIlIIIIll) // 2
    if lllllIIIllIlIllIIl == llIlIlIIIlIllIlllI[IIIlIllllIlllIII]:         
      return True
    elif lllllIIIllIlIllIIl < llIlIlIIIlIllIlllI[IIIlIllllIlllIII]:
      return llIIIIIIlIlllII(llIlIlIIIlIllIlllI, lllllIIIllIlIllIIl, lllIIIlIlII, IIIlIllllIlllIII - 1)
    else:
      return llIIIIIIlIlllII(llIlIlIIIlIllIlllI, lllllIIIllIlIllIIl, IIIlIllllIlllIII + 1, IIlIIIIll)