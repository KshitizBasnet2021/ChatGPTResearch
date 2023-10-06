#mutation_10_line_no_6_ROR.py
#
#Yes, there is a bug in the provided code. The condition in the while loop is incorrect. It should be "IIlIIllIIIlllIllIllI < IIlIllIIIIIIlIll" instead of "IIlIIllIIIlllIllIllI > IIlIllIIIIIIlIll". 
#
#Here is the corrected code:
#
def llIlIIlIIlIllllII(IIlIIllIlIIIlllIIIl, lIIllIllII):
  IIIlllIIllIl, IIlIllIIIIIIlIll = len(IIlIIllIlIIIlllIIIl), len(lIIllIllII)                      
  for llIIIlIIllIII in range(IIIlllIIllIl-IIlIllIIIIIIlIll+1):                     
    IIlIIllIIIlllIllIllI = 0                                    
    while (IIlIIllIIIlllIllIllI < IIlIllIIIIIIlIll and IIlIIllIlIIIlllIIIl[llIIIlIIllIII + IIlIIllIIIlllIllIllI] == lIIllIllII[IIlIIllIIIlllIllIllI]):
      IIlIIllIIIlllIllIllI += 1
    if IIlIIllIIIlllIllIllI == IIlIllIIIIIIlIll:                               
      return llIIIlIIllIII                               
  return -1                                  
#
#
#