#mutation_8_line_no_8_COI.py
#
#There is a bug in the provided code. The bug is in the line `if not (llIIllIlIIlll == lIllllIIlll):`. This condition is checking if the length of the matched substring is not equal to the length of the pattern. However, it should be checking if the length of the matched substring is equal to the length of the pattern. 
#
#Here is the corrected code:
#
def IlIIIIlIIIIl(lIIIIlIIllIIIlIlIlI, lIlIIIllIllIlIl):
  lIIlllIIlIlIlll, lIllllIIlll = len(lIIIIlIIllIIIlIlIlI), len(lIlIIIllIllIlIl)                      
  for IlllIIlllIllIlIIlll in range(lIIlllIIlIlIlll-lIllllIIlll+1):                     
    llIIllIlIIlll = 0                                    
    while llIIllIlIIlll < lIllllIIlll and lIIIIlIIllIIIlIlIlI[IlllIIlllIllIlIIlll + llIIllIlIIlll] == lIlIIIllIllIlIl[llIIllIlIIlll]:        
      llIIllIlIIlll += 1
    if llIIllIlIIlll == lIllllIIlll:
      return IlllIIlllIllIlIIlll                               
  return -1                                  
#
#
#