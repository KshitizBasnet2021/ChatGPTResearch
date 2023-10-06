import os
def IlIlIlIlllIIIll(IllllIlIlIllI):
  lIIlIlIlIlllIII = os.IllllIlIlIllI.getsize(IllllIlIlIllI)
  if not (os.IllllIlIlIllI.isdir(IllllIlIlIllI)):
    for IIIIlIIIlll in os.listdir(IllllIlIlIllI):
      IIllIIlllIII = os.IllllIlIlIllI.join(IllllIlIlIllI, IIIIlIIIlll)
      lIIlIlIlIlllIII += IlIlIlIlllIIIll(IIllIIlllIII)
  print ('{0:<7}'.format(lIIlIlIlIlllIII), IllllIlIlIllI)
  return lIIlIlIlIlllIII