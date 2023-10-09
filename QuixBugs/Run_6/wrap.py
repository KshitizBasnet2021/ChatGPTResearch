#wrap.py
#
#Yes, there is a bug in the provided code. The line `IlllIIIlllIllIIIlI = IlllIIIlllIllIIIlI[lllIIIllIlIllIlIll:]` should be changed to `IlllIIIlllIllIIIlI = IlllIIIlllIllIIIlI[lllIIIllIlIllIlIll+1:]` in order to remove the space character from the beginning of the next substring.
#
#Here is the corrected code:
#
def wrap(IlllIIIlllIllIIIlI, IlIllIIlIIIlIIlIIII):
    IllIlllIl = []
    while len(IlllIIIlllIllIIIlI) > IlIllIIlIIIlIIlIIII:
        lllIIIllIlIllIlIll = IlllIIIlllIllIIIlI.rfind(' ', 0, IlIllIIlIIIlIIlIIII + 1)
        if lllIIIllIlIllIlIll == -1:
            lllIIIllIlIllIlIll = IlIllIIlIIIlIIlIIII
        IllllIIIllIII, IlllIIIlllIllIIIlI = IlllIIIlllIllIIIlI[:lllIIIllIlIllIlIll], IlllIIIlllIllIIIlI[lllIIIllIlIllIlIll+1:]
        IllIlllIl.append(IllllIIIllIII)
    return IllIlllIl
#
#
#