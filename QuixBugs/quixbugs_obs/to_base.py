import string
def IllIIllIIIlIIlIlll(llIllIlllIIIIIllIIl, IIlIlIllIIl):
    IIIlIllIIlIllIIlIl = ''
    IllIIIIIIlIlI = string.digits + string.ascii_uppercase
    while llIllIlllIIIIIllIIl > 0:
        llIIIIIl = llIllIlllIIIIIllIIl % IIlIlIllIIl
        llIllIlllIIIIIllIIl = llIllIlllIIIIIllIIl // IIlIlIllIIl
        IIIlIllIIlIllIIlIl = IIIlIllIIlIllIIlIl + IllIIIIIIlIlI[llIIIIIl]
    return IIIlIllIIlIllIIlIl