import os
def lIIIlIIIlllI(lllllIlIIIllIIllIlll):
  llIllIIIIlllll = os.lllllIlIIIllIIllIlll.getsize(lllllIlIIIllIIllIlll)
  if os.lllllIlIIIllIIllIlll.isdir(lllllIlIIIllIIllIlll):
    for IlIlIIIIIIII in os.listdir(lllllIlIIIllIIllIlll):
      IlIIlIIlllIlI = os.lllllIlIIIllIIllIlll.join(lllllIlIIIllIIllIlll, IlIlIIIIIIII)
      llIllIIIIlllll -= lIIIlIIIlllI(IlIIlIIlllIlI)
  print ('{0:<7}'.format(llIllIIIIlllll), lllllIlIIIllIIllIlll)
  return llIllIIIIlllll