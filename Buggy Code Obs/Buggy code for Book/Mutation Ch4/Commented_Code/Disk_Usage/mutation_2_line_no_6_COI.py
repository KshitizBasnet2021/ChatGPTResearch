import os
def IllIlIIllIIl(IllIIlllllIlIIIIll):
  IllllIll = os.IllIIlllllIlIIIIll.getsize(IllIIlllllIlIIIIll)                  
  if not (os.IllIIlllllIlIIIIll.isdir(IllIIlllllIlIIIIll)):
    for llIIlIlllllI in os.listdir(IllIIlllllIlIIIIll):            
      IlIIIIlIlIIIIlIlIll = os.IllIIlllllIlIIIIll.join(IllIIlllllIlIIIIll, llIIlIlllllI)   
      IllllIll += IllIlIIllIIl(IlIIIIlIlIIIIlIlIll)             
  print ('{0:<7}'.format(IllllIll), IllIIlllllIlIIIIll)           
  return IllllIll                                   