#mutation_4_line_no_5_AOR.py
#
#The provided code is a recursive implementation of the QuickSort algorithm. However, there is a bug in the code. 
#
#The bug is in the recursive call to `llllIIIlIIllllIIIlll` function. The second argument `IlIIIIlIllIIIlllI - 1` should be `IlIIIIlIllIIIlllI`, and the third argument `IIllIIlIllIIIIl - 1` should be `IIllIIlIllIIIIl - 2`. 
#
#Here's the corrected code:
#
def llllIIIlIIllllIIIlll(lIIlllIll, IlIIIIlIllIIIlllI, IIllIIlIllIIIIl):
  if IlIIIIlIllIIIlllI < IIllIIlIllIIIIl - 1:                         
    lIIlllIll[IlIIIIlIllIIIlllI], lIIlllIll[IIllIIlIllIIIIl-1] = lIIlllIll[IIllIIlIllIIIIl-1], lIIlllIll[IlIIIIlIllIIIlllI]  
    llllIIIlIIllllIIIlll(lIIlllIll, IlIIIIlIllIIIlllI, IIllIIlIllIIIIl - 2)
#
#Now the code should work correctly.
#
#
#