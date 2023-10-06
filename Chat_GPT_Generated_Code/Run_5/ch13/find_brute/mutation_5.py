#mutation_5_line_no_10_AOR.py
#
#There is a bug in the provided code. The bug is in the return statement at the end of the function. The code is returning `+1` instead of `-1` when the substring is not found in the main string. 
#
#Here's the corrected code:
#
#```python
def lIlIIllIIllllIIlIIII(lllIllIlIlIIlllIl, IIIlIlIIIlI):
  llIllIlll, IIlIlIIIlllll = len(lllIllIlIlIIlllIl), len(IIIlIlIIIlI)                      
  for lIlllIIlllI in range(llIllIlll-IIlIlIIIlllll+1):                     
    IIllIllIlIIIlIIIIlIl = 0                                    
    while IIllIllIlIIIlIIIIlIl < IIlIlIIIlllll and lllIllIlIlIIlllIl[lIlllIIlllI + IIllIllIlIIIlIIIIlIl] == IIIlIlIIIlI[IIllIllIlIIIlIIIIlIl]:        
      IIllIllIlIIIlIIIIlIl += 1
    if IIllIllIlIIIlIIIIlIl == IIlIlIIIlllll:                               
      return lIlllIIlllI                               
  return -1
#```
#
#Now, the function will return -1 if the substring is not found in the main string.
#
#
#