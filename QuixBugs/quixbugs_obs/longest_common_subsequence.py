def lIIIllIII(lllIIIlII, IIIlIIIIlIIllIlll):
    if not lllIIIlII or not IIIlIIIIlIIllIlll:
        return ''
    elif lllIIIlII[0] == IIIlIIIIlIIllIlll[0]:
        return lllIIIlII[0] + lIIIllIII(lllIIIlII[1:], IIIlIIIIlIIllIlll)
    else:
        return max(
            lIIIllIII(lllIIIlII, IIIlIIIIlIIllIlll[1:]),
            lIIIllIII(lllIIIlII[1:], IIIlIIIIlIIllIlll),
            key=len
        )