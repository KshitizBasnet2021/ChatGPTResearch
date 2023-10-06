#mutation_2_line_no_4_AOR.py
#
#Yes, there is a bug in the provided code. The bug is in the line where the swap is happening:
#
#(lIIlIIlllIlIllI[IlllIlIIlllIl], lIIlIIlllIlIllI[llllIlllllIl + 1]) = (lIIlIIlllIlIllI[llllIlllllIl - 1], lIIlIIlllIlIllI[IlllIlIIlllIl])
#
#The indices used for swapping are incorrect. It should be:
#
#(lIIlIIlllIlIllI[IlllIlIIlllIl], lIIlIIlllIlIllI[IlllIlIIlllIl + 1]) = (lIIlIIlllIlIllI[IlllIlIIlllIl + 1], lIIlIIlllIlIllI[IlllIlIIlllIl])
#
#Here's the corrected code:
#
def lIlIlllllIlII(lIIlIIlllIlIllI, IlllIlIIlllIl, llllIlllllIl):
  if IlllIlIIlllIl < llllIlllllIl - 1:                         
    (lIIlIIlllIlIllI[IlllIlIIlllIl], lIIlIIlllIlIllI[IlllIlIIlllIl + 1]) = (lIIlIIlllIlIllI[IlllIlIIlllIl + 1], lIIlIIlllIlIllI[IlllIlIIlllIl])
    lIlIlllllIlII(lIIlIIlllIlIllI, IlllIlIIlllIl+1, llllIlllllIl-1)
#
#
#