#mutation_7_line_no_5_COI.py
#
#There is a bug in the provided code. The condition in the while loop is incorrect. It should be "while llIllllII <= IIIIllIIIIllIIlIllI:" instead of "while not (llIllllII <= IIIIllIIIIllIIlIllI):". 
#
#Here is the corrected code:
#
def IlIIlIIIllIIIlllIlI(lllIlIlIIlllIIlI, lIlIIIlIIIIlIIll):
  llIllllII = 0
  IIIIllIIIIllIIlIllI = len(lllIlIlIIlllIIlI)-1
  while llIllllII <= IIIIllIIIIllIIlIllI:
    IlIIlIIlllIlIlII = (llIllllII + IIIIllIIIIllIIlIllI) // 2
    if lIlIIIlIIIIlIIll == lllIlIlIIlllIIlI[IlIIlIIlllIlIlII]:         
      return True
    elif lIlIIIlIIIIlIIll < lllIlIlIIlllIIlI[IlIIlIIlllIlIlII]:
      IIIIllIIIIllIIlIllI = IlIIlIIlllIlIlII - 1                
    else:
      llIllllII = IlIIlIIlllIlIlII + 1                 
  return False
#
#
#