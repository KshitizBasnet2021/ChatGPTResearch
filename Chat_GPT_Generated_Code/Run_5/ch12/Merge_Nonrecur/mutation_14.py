#mutation_14_line_no_11_ASR.py
#
#There is a bug in the code. In the function `lllIllllllllIllllII`, the variable `IlIIIIIlllI` is misspelled as `IlIIIIIlllI` in multiple places. 
#
#Here is the corrected code:
#
import math
#
def lllIllllllllIllllII(IlIIIIIlllI, lllIIllllIlIIlIIlI, lIllIIIlIlllIIlIIlI, lIIlIllIll):
  lIIlIIllIIIlIlIlII = lIllIIIlIlllIIlIIlI + lIIlIllIll
  IIIIlIllIIlll = min(lIllIIIlIlllIIlIIlI + 2 * lIIlIllIll, len(IlIIIIIlllI))
  lllIIIllIIl, IlIIlIlIlII, IIIlllllIl = lIllIIIlIlllIIlIIlI, lIllIIIlIlllIIlIIlI + lIIlIllIll, lIllIIIlIlllIIlIIlI
  while lllIIIllIIl < lIIlIIllIIIlIlIlII and IlIIlIlIlII < IIIIlIllIIlll:
    if IlIIIIIlllI[lllIIIllIIl] < IlIIIIIlllI[IlIIlIlIlII]:
      lllIIllllIlIIlIIlI[IIIlllllIl] = IlIIIIIlllI[lllIIIllIIl]
      lllIIIllIIl -= 1
    else:
      lllIIllllIlIIlIIlI[IIIlllllIl] = IlIIIIIlllI[IlIIlIlIlII]
      IlIIlIlIlII += 1
    IIIlllllIl += 1
  if lllIIIllIIl < lIIlIIllIIIlIlIlII:
    lllIIllllIlIIlIIlI[IIIlllllIl:IIIIlIllIIlll] = IlIIIIIlllI[lllIIIllIIl:lIIlIIllIIIlIlIlII]
  elif IlIIlIlIlII < IIIIlIllIIlll:
    lllIIllllIlIIlIIlI[IIIlllllIl:IIIIlIllIIlll] = IlIIIIIlllI[IlIIlIlIlII:IIIIlIllIIlll]
#
def IIIllIlIIIlIIlII(lIlllIlIlIl):
  lIllIlIlll = len(lIlllIlIlIl)
  Illllllll = math.ceil(math.log(lIllIlIlll, 2))
  IlIIIIIlllI, IllIIllllI = lIlllIlIlIl, [None] * lIllIlIlll
  for IIlIllIlIIIIIIIII in (2**IIlllllI for IIlllllI in range(Illllllll)):
    for IlllllIlIIllIlIIlllI in range(0, lIllIlIlll, 2 * IIlIllIlIIIIIIIII):
      lllIllllllllIllllII(IlIIIIIlllI, IllIIllllI, IlllllIlIIllIlIIlllI, IIlIllIlIIIIIIIII)
    IlIIIIIlllI, IllIIllllI = IllIIllllI, IlIIIIIlllI
  if lIlllIlIlIl is not IlIIIIIlllI:
    lIlllIlIlIl[0:lIllIlIlll] = IlIIIIIlllI[0:lIllIlIlll]
#
#
#