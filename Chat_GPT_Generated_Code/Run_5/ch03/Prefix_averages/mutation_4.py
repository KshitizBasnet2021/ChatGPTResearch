#mutation_4_line_no_8_AOR.py
#
#The code provided has a bug. The variable `IlIIIlllIIlIIIlIIIll` is initialized as a list of zeros with a length equal to `IllIIlIllIllIl`, but it should be initialized as an empty list instead. 
#
#Here's the corrected code:
#
def lIllllIlllllIIlIIlIl(lIllIIlI):
  IllIIlIllIllIl = len(lIllIIlI)
  IlIIIlllIIlIIIlIIIll = []                   
  IIIlIIIIllIIlllI = 0                     
  for lIlIlllIlIIlIIl in range(IllIIlIllIllIl):
    IIIlIIIIllIIlllI += lIllIIlI[lIlIlllIlIIlIIl]               
    IlIIIlllIIlIIIlIIIll.append(IIIlIIIIllIIlllI // (lIlIlllIlIIlIIl + 1))
  return IlIIIlllIIlIIIlIIIll
#
#
#