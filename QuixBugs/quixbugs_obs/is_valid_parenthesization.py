def IlIllllIIIllIlIl(lIllIlIIIllII):
    IlllIIlIIlIl = 0
    for IlIlIIlIllIllI in lIllIlIIIllII:
        if IlIlIIlIllIllI == '(':
            IlllIIlIIlIl += 1
        else:
            IlllIIlIIlIl -= 1
            if IlllIIlIIlIl < 0:
                return False
    return True