#mutation_3_line_no_4_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the line where the swap is happening:
#
#(lIlllIllI[llIIlIlII], lIlllIllI[lIlIIIll - 1]) = (lIlllIllI[lIlIIIll + 1], lIlllIllI[llIIlIlII])
#
#The indices used for swapping are incorrect. It should be:
#
#(lIlllIllI[llIIlIlII], lIlllIllI[lIlIIIll - 1]) = (lIlllIllI[lIlIIIll - 1], lIlllIllI[llIIlIlII])
#
#Here's the corrected code:
#
def lIllIIIIlI(lIlllIllI, llIIlIlII, lIlIIIll):
  if llIIlIlII < lIlIIIll - 1:                         
    (lIlllIllI[llIIlIlII], lIlllIllI[lIlIIIll - 1]) = (lIlllIllI[lIlIIIll - 1], lIlllIllI[llIIlIlII])
    lIllIIIIlI(lIlllIllI, llIIlIlII+1, lIlIIIll-1)
#
#
#