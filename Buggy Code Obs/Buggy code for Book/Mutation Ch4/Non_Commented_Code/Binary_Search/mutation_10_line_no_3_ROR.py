def IIlllIllIlIllIllll(IIlllIIIl, IlllIIIIlllllII, IIIIllllllIIlII, IIlllIlIll):
  if IIIIllllllIIlII >= IIlllIlIll:
    return False
  else:
    lIllIlIlIIlIlIIlll = (IIIIllllllIIlII + IIlllIlIll) // 2
    if IlllIIIIlllllII == IIlllIIIl[lIllIlIlIIlIlIIlll]:
      return True
    elif IlllIIIIlllllII < IIlllIIIl[lIllIlIlIIlIlIIlll]:
      return IIlllIllIlIllIllll(IIlllIIIl, IlllIIIIlllllII, IIIIllllllIIlII, lIllIlIlIIlIlIIlll - 1)
    else:
      return IIlllIllIlIllIllll(IIlllIIIl, IlllIIIIlllllII, lIllIlIlIIlIlIIlll + 1, IIlllIlIll)