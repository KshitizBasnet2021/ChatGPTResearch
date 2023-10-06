#mutation_2_line_no_4_AOR.py
#
#Yes, there is a bug in the provided code. 
#
#The bug is in the line `IIIIllIlIllIl = [0] // IIIlIlIlI`. The double forward slashes (`//`) are used for integer division in Python, but in this case, it seems like it was intended to create a list with a single element of 0. 
#
#To fix this bug, we can change the line to `IIIIllIlIllIl = [0] * IIIlIlIlI` to create a list with `IIIlIlIlI` number of elements, all initialized to 0. 
#
#Here is the corrected code:
#
def IIlIIIllI(IIIlIIllIIII):
  IIIlIlIlI = len(IIIlIIllIIII)
  IIIIllIlIllIl = [0] * IIIlIlIlI
  IIIllIIIIlIII = 0                     
  for lIllIIIIllII in range(IIIlIlIlI):
    IIIllIIIIlIII += IIIlIIllIIII[lIllIIIIllII]               
    IIIIllIlIllIl[lIllIIIIllII] = IIIllIIIIlIII / (lIllIIIIllII+1)        
  return IIIIllIlIllIl
#
#
#