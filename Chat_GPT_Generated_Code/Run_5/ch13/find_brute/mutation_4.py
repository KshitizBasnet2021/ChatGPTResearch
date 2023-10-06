#mutation_4_line_no_6_AOR.py
#
#There is a bug in the provided code. The variable `lIIIIIIllIl` is used as an index in the line `while (llllllIIlIIl < llIlllIIllIl and llIlIIllIlIlIllllll[lIIIIIIllIl - llllllIIlIIl] == lIlIIIlIIllIl[llllllIIlIIl]):`, but it should be `lIIIIIIllIl + llllllIIlIIl` instead. 
#
#Here is the corrected code:
#
def llIIllIllIlIlIl(llIlIIllIlIlIllllll, lIlIIIlIIllIl):
  IllIIIIIIlIIllIllI, llIlllIIllIl = len(llIlIIllIlIlIllllll), len(lIlIIIlIIllIl)                      
  for lIIIIIIllIl in range(IllIIIIIIlIIllIllI-llIlllIIllIl+1):                     
    llllllIIlIIl = 0                                    
    while (llllllIIlIIl < llIlllIIllIl and llIlIIllIlIlIllllll[lIIIIIIllIl + llllllIIlIIl] == lIlIIIlIIllIl[llllllIIlIIl]):
      llllllIIlIIl += 1
    if llllllIIlIIl == llIlllIIllIl:                               
      return lIIIIIIllIl                               
  return -1
#
#
#