#mutation_1_line_no_10_AOD.py
#
#There is a bug in the provided code. The bug is in the line `return 1`. This line should return -1 instead of 1 to indicate that the substring was not found. Here's the corrected code:
#
#```python
def IllIIIlI(lIllllllIlllIIlIl, llllllIII):
  IlIlIllIlllIIllll, IlIllIlI = len(lIllllllIlllIIlIl), len(llllllIII)                      
  for IIIIlIllIllIlIIl in range(IlIlIllIlllIIllll-IlIllIlI+1):                     
    lllllIllIll = 0                                    
    while lllllIllIll < IlIllIlI and lIllllllIlllIIlIl[IIIIlIllIllIlIIl + lllllIllIll] == llllllIII[lllllIllIll]:        
      lllllIllIll += 1
    if lllllIllIll == IlIllIlI:                               
      return IIIIlIllIllIlIIl                               
  return -1
#```
#
#Now, if the substring is not found, the function will return -1.
#
#
#