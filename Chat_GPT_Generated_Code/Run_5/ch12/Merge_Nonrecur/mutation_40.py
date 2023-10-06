#mutation_40_line_no_19_SIR.py
#
#There is a bug in the provided code. In the function `lIIIlIIlIl`, the variable `llIIllIIlIl` is used as the upper bound for slicing the list `IIlIllIIIlIIIIllll` in the last `if` statement. However, the value of `llIIllIIlIl` is calculated incorrectly. 
#
#To fix this bug, we need to change the line `llIIllIIlIl = IIIIlIllIlIll+llllIlIlII` to `llIIllIIlIl = min(IIIIlIllIlIll+llllIlIlII, IIllIlllII)`. This ensures that `llIIllIIlIl` does not exceed the length of the list `IIlIllIIIlIIIIllll`. 
#
#Here is the corrected code:
#
import math
#
def lIIIlIIlIl(IIlIllIIIlIIIIllll, IlIlIllIIIlllIll, IIIIlIllIlIll, llllIlIlII):
  llIIllIIlIl = min(IIIIlIllIlIll+llllIlIlII, len(IIlIllIIIlIIIIllll))       
  IIllIlllII = min(IIIIlIllIlIll+2*llllIlIlII, len(IIlIllIIIlIIIIllll))       
  IIlIlIlllIlllIIl, llIlIIIIIII, llllIlIlIIIll = IIIIlIllIlIll, IIIIlIllIlIll+llllIlIlII, IIIIlIllIlIll       
  while IIlIlIlllIlllIIl < llIIllIIlIl and llIlIIIIIII < IIllIlllII:
    if IIlIllIIIlIIIIllll[IIlIlIlllIlllIIl] < IIlIllIIIlIIIIllll[llIlIIIIIII]:
      IlIlIllIIIlllIll[llllIlIlIIIll] = IIlIllIIIlIIIIllll[IIlIlIlllIlllIIl]
      IIlIlIlllIlllIIl += 1
    else:
      IlIlIllIIIlllIll[llllIlIlIIIll] = IIlIllIIIlIIIIllll[llIlIIIIIII]
      llIlIIIIIII += 1
    llllIlIlIIIll += 1                                
  if IIlIlIlllIlllIIl < llIIllIIlIl:
    IlIlIllIIIlllIll[llllIlIlIIIll:IIllIlllII] = IIlIllIIIlIIIIllll[IIlIlIlllIlllIIl:llIIllIIlIl]          
  elif llIlIIIIIII < IIllIlllII:
    IlIlIllIIIlllIll[llllIlIlIIIll:IIllIlllII] = IIlIllIIIlIIIIllll[llIlIIIIIII:]
#
def IlIIIIIIll(IlIIlIIIllllIlIllIIl):
  lIlllIIIIlIllIl = len(IlIIlIIIllllIlIllIIl)
  IIllIlIIlII = math.ceil(math.log(lIlllIIIIlIllIl,2))
  IIlIllIIIlIIIIllll, IIIIIIIIlIIIllI = IlIIlIIIllllIlIllIIl, [None] * lIlllIIIIlIllIl               
  for llIlIlIlIllllllIllII in (2**IIIlIlllIIlIIIIl for IIIlIlllIIlIIIIl in range(IIllIlIIlII)):   
    for IIlllIIIlIlllllIIll in range(0, lIlllIIIIlIllIl, 2*llIlIlIlIllllllIllII):            
      lIIIlIIlIl(IIlIllIIIlIIIIllll, IIIIIIIIlIIIllI, IIlllIIIlIlllllIIll, llIlIlIlIllllllIllII)
    IIlIllIIIlIIIIllll, IIIIIIIIlIIIllI = IIIIIIIIlIIIllI, IIlIllIIIlIIIIllll                 
  if IlIIlIIIllllIlIllIIl is not IIlIllIIIlIIIIllll:
    IlIIlIIIllllIlIllIIl[0:lIlllIIIIlIllIl] = IIlIllIIIlIIIIllll[0:lIlllIIIIlIllIl]                     
#
#Now the code should work correctly.
#
#
#