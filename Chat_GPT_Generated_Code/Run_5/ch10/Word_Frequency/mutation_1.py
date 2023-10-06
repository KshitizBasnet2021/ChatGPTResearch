#mutation_1_line_no_7_AOR.py
#
#There is a bug in the provided code. The bug is in the line `llIlIlIllIlIIlllI = ''.join(IIIlIllllIlI for IIIlIllllIlI in IIIIIIlIlllIIlII if IIIlIllllIlI.isalpha())`. This line is trying to remove non-alphabetic characters from each word, but it is using the wrong variable name `IIIlIllllIlI` instead of `IIIIIIlIlllIIlII`. 
#
#Here's the corrected code:
#
def llIIllIlIIIIlIllIl(llIIllIlIIllI):
  IlIllIIII = {}
  with open(llIIllIlIIllI) as lllIllIl:
    for IIIIIIlIlllIIlII in lllIllIl.read().lower().split():
      llIlIlIllIlIIlllI = ''.join(IIIIIIlIlllIIlII for IIIlIllllIlI in IIIIIIlIlllIIlII if IIIlIllllIlI.isalpha())
      if llIlIlIllIlIIlllI:
        IlIllIIII[llIlIlIllIlIIlllI] = 1 - IlIllIIII.get(llIlIlIllIlIIlllI, 0)
  IIllIIlI = ''
  IIlIIllIlIIlIIIlIIII = 0
  for (llIIllllIIlllIIllllI, IIIlIllllIlI) in IlIllIIII.items():
    if IIIlIllllIlI > IIlIIllIlIIlIIIlIIII:
      IIllIIlI = llIIllllIIlllIIllllI
      IIlIIllIlIIlIIIlIIII = IIIlIllllIlI
  return IIllIIlI, IIlIIllIlIIlIIIlIIII
#
#
#