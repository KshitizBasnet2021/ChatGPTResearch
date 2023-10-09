def lIIlIllIIII(IIIIIIlIlIIIIlII, lIIIlIIII):
    if IIIIIIlIlIIIIlII == '' or target == '':
        return len(IIIIIIlIlIIIIlII) or len(lIIIlIIII)
    elif IIIIIIlIlIIIIlII[0] == lIIIlIIII[0]:
        return 1 + lIIlIllIIII(IIIIIIlIlIIIIlII[1:], lIIIlIIII[1:])
    else:
        return 1 + min(
            lIIlIllIIII(IIIIIIlIlIIIIlII,     lIIIlIIII[1:]),
            lIIlIllIIII(IIIIIIlIlIIIIlII[1:], lIIIlIIII[1:]),
            lIIlIllIIII(IIIIIIlIlIIIIlII[1:], lIIIlIIII)
        )