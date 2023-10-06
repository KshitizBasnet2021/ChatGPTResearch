#mutation_10_line_no_26_AOR.py
#
#There is a bug in the code. In the function `lIIIlllIIII`, the variable `IIllIlIIIIlIlll` is defined as a parameter, but it is used as a list inside the function. This will cause an error when trying to assign values to it. 
#
#To fix this, you can either remove the parameter `IIllIlIIIIlIlll` and define it as an empty list inside the function, or you can pass it as an argument when calling the function. 
#
#Here is the corrected code:
#
import math
#
def lIIIlllIIII(IIllIIlIIIlllIl, IIllIlIIIIlIlll, IIlllIIIIIlIIIII, lIIIlIIIIIIlIllIlll):
  IIIIIIlIlIIllIIlIlll = IIlllIIIIIlIIIII+lIIIlIIIIIIlIllIlll                        
  lIllllllIIIll = min(IIlllIIIIIlIIIII+2*lIIIlIIIIIIlIllIlll, len(IIllIIlIIIlllIl))       
  IIllllIIIIllIIll, lIIllllIlllIll, IllIIlIlllllI = IIlllIIIIIlIIIII, IIlllIIIIIlIIIII+lIIIlIIIIIIlIllIlll, IIlllIIIIIlIIIII       
  while IIllllIIIIllIIll < IIIIIIlIlIIllIIlIlll and lIIllllIlllIll < lIllllllIIIll:
    if IIllIIlIIIlllIl[IIllllIIIIllIIll] < IIllIIlIIIlllIl[lIIllllIlllIll]:
      IIllIlIIIIlIlll[IllIIlIlllllI] = IIllIIlIIIlllIl[IIllllIIIIllIIll]
      IIllllIIIIllIIll += 1
    else:
      IIllIlIIIIlIlll[IllIIlIlllllI] = IIllIIlIIIlllIl[lIIllllIlllIll]
      lIIllllIlllIll += 1
    IllIIlIlllllI += 1                                
  if IIllllIIIIllIIll < IIIIIIlIlIIllIIlIlll:
    IIllIlIIIIlIlll[IllIIlIlllllI:lIllllllIIIll] = IIllIIlIIIlllIl[IIllllIIIIllIIll:IIIIIIlIlIIllIIlIlll]          
  elif lIIllllIlllIll < lIllllllIIIll:
    IIllIlIIIIlIlll[IllIIlIlllllI:lIllllllIIIll] = IIllIIlIIIlllIl[lIIllllIlllIll:lIllllllIIIll]          
#
def lIIIllIlIll(IIIlIIIlIllIlllIllIl):
  lIIllIlI = len(IIIlIIIlIllIlllIllIl)
  llIllllIlIllIl = math.ceil(math.log(lIIllIlI,2))
  IIllIIlIIIlllIl, lIIIIlIIlIlllllllll = IIIlIIIlIllIlllIllIl, [None] * lIIllIlI               
  for lIIIIllIlIlIIII in (2 * lIlIlllIIllII for lIlIlllIIllII in range(llIllllIlIllIl)):
    for IlllIIIIllllllllIllI in range(0, lIIllIlI, 2*lIIIIllIlIlIIII):            
      lIIIlllIIII(IIllIIlIIIlllIl, lIIIIlIIlIlllllllll, IlllIIIIllllllllIllI, lIIIIllIlIlIIII)
    IIllIIlIIIlllIl, lIIIIlIIlIlllllllll = lIIIIlIIlIlllllllll, IIllIIlIIIlllIl                 
  if IIIlIIIlIllIlllIllIl is not IIllIIlIIIlllIl:
    IIIlIIIlIllIlllIllIl[0:lIIllIlI] = IIllIIlIIIlllIl[0:lIIllIlI]                     
#
## Example usage
#arr = [4, 2, 7, 1, 5]
#lIIIllIlIll(arr)
#print(arr)
#
#
#