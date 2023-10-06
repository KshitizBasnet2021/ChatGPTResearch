#mutation_9_line_no_6_LCR.py
#
#There is a bug in the provided code. The while loop condition should be modified to check if `IlllIIIIIllIlIIIll` is less than `IllllIIlIIIIl` and if the characters at the corresponding positions in the two strings are equal. Additionally, the loop should terminate if `IIlIllIIIIIllIIIl + IlllIIIIIllIlIIIll` exceeds the length of `lIlIlIllIIIIII`. 
#
#Here is the corrected code:
#
def IIllllIIlIII(lIlIlIllIIIIII, IlIllllIIlIlII):
  IllIIIIlIl, IllllIIlIIIIl = len(lIlIlIllIIIIII), len(IlIllllIIlIlII)                      
  for IIlIllIIIIIllIIIl in range(IllIIIIlIl-IllllIIlIIIIl+1):                     
    IlllIIIIIllIlIIIll = 0                                    
    while (IlllIIIIIllIlIIIll < IllllIIlIIIIl and IIlIllIIIIIllIIIl + IlllIIIIIllIlIIIll < IllIIIIlIl and lIlIlIllIIIIII[IIlIllIIIIIllIIIl + IlllIIIIIllIlIIIll] == IlIllllIIlIlII[IlllIIIIIllIlIIIll]):
      IlllIIIIIllIlIIIll += 1
    if IlllIIIIIllIlIIIll == IllllIIlIIIIl:                               
      return IIlIllIIIIIllIIIl                               
  return -1
#
#
#