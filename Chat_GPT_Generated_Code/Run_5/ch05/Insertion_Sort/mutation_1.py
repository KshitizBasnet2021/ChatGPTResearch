#mutation_1_line_no_6_AOR.py
#
#Yes, there is a bug in the provided code. The line `lIllIlIIIIl[lllIllllIllllIllll] = lIllIlIIIIl[lllIllllIllllIllll-1]` should be `lIllIlIIIIl[lllIllllIllllIllll] = lIllIlIIIIl[lllIllllIllllIllll-1]`. The index should be `lllIllllIllllIllll-1` instead of `lllIllllIllllIllll+1`. 
#
#Here is the corrected code:
#
def llIlIllIIIlllIllIII(lIllIlIIIIl):
  for IIlIIIll in range(1, len(lIllIlIIIIl)):         
    IIIIIllI = lIllIlIIIIl[IIlIIIll]                       
    lllIllllIllllIllll = IIlIIIll                            
    while (lllIllllIllllIllll > 0 and lIllIlIIIIl[lllIllllIllllIllll - 1] > IIIIIllI):
      lIllIlIIIIl[lllIllllIllllIllll] = lIllIlIIIIl[lllIllllIllllIllll-1]
      lllIllllIllllIllll -= 1
    lIllIlIIIIl[lllIllllIllllIllll] = IIIIIllI
#
#
#