import os
def llIIlIlIlIlII(IllllIIlIIIl):
  lIlIIIlll = os.IllllIIlIIIl.getsize(IllllIIlIIIl)                  
  if os.IllllIIlIIIl.isdir(IllllIIlIIIl):                        
    for llIIIIIlllIlIIl in os.listdir(IllllIIlIIIl):            
      lllIIIIllIIIlllll = os.IllllIIlIIIl.join(IllllIIlIIIl, llIIIIIlllIlIIl)   
      lIlIIIlll -= llIIlIlIlIlII(lllIIIIllIIIlllll)
  print ('{0:<7}'.format(lIlIIIlll), IllllIIlIIIl)           
  return lIlIIIlll                                   