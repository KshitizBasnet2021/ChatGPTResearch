#mutation_9_line_no_9_COI.py
#
#There is a bug in the provided code. The bug is in the line `elif not (lIlIIIIllIIIllIIllII < IIllIIllIIl[IIIllIIlIl]):`. The condition should be `elif not (lIlIIIIllIIIllIIllII > IIllIIllIIl[IIIllIIlIl]):` instead.
#
#Here is the corrected code:
#
def lIllIllllIlIlIII(IIllIIllIIl, lIlIIIIllIIIllIIllII):
  IllIlIIIlIll = 0
  IIIIIllIlIIIlII = len(IIllIIllIIl)-1
  while IllIlIIIlIll <= IIIIIllIlIIIlII:
    IIIllIIlIl = (IllIlIIIlIll + IIIIIllIlIIIlII) // 2
    if lIlIIIIllIIIllIIllII == IIllIIllIIl[IIIllIIlIl]:         
      return True
    elif not (lIlIIIIllIIIllIIllII > IIllIIllIIl[IIIllIIlIl]):
      IIIIIllIlIIIlII = IIIllIIlIl - 1                
    else:
      IllIlIIIlIll = IIIllIIlIl + 1                 
  return False
#
#
#