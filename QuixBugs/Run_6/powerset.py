#powerset.py
#
#The provided code is missing a colon at the end of the first line. Here is the corrected code:
#
def powerset(lIIllIIIIlIlI):
    if lIIllIIIIlIlI:
        llIlIlIllllIIIII, *IllIIIIIllIIlIl = lIIllIIIIlIlI 
        IlIIIllIllIl = IIIlIlIlIIIII(IllIIIIIllIIlIl)
        return [[llIlIlIllllIIIII] + IllIIIllIIIlIIl for IllIIIllIIIlIIl in IlIIIllIllIl]
    else:
        return [[]]
#
#
#