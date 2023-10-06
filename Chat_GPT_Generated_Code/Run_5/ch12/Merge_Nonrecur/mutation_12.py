#mutation_12_line_no_27_AOR.py
#
#There is a bug in the code. In the function `IllIIllIIllllIII`, the variable `IIlllIIIIlIlIIII` is incorrectly calculated. It should be `min(llIIlIIlllIIllllIll+2*IIIlIllII, len(llIIlIIlllIIllllIll))` instead of `min(llIIlIIlllIIllllIll+2*IIIlIllII, len(llIIlIIll))`.
#
#Here is the corrected code:
#
import math
#
def IllIIllIIllllIII(llIIlIIll, IIlIIlIlIIlIllII, llIIlIIlllIIllllIll, IIIlIllII):
  IlIIIlIIIlIIll = llIIlIIlllIIllllIll+IIIlIllII                        
  IIlllIIIIlIlIIII = min(llIIlIIlllIIllllIll+2*IIIlIllII, len(llIIlIIlllIIllllIll))       
  IllIIIllIIIIl, lIIlIlllIl, IIllllII = llIIlIIlllIIllllIll, llIIlIIlllIIllllIll+IIIlIllII, llIIlIIlllIIllllIll       
  while IllIIIllIIIIl < IlIIIlIIIlIIll and lIIlIlllIl < IIlllIIIIlIlIIII:
    if llIIlIIll[IllIIIllIIIIl] < llIIlIIll[lIIlIlllIl]:
      IIlIIlIlIIlIllII[IIllllII] = llIIlIIll[IllIIIllIIIIl]
      IllIIIllIIIIl += 1
    else:
      IIlIIlIlIIlIllII[IIllllII] = llIIlIIll[lIIlIlllIl]
      lIIlIlllIl += 1
    IIllllII += 1                                
  if IllIIIllIIIIl < IlIIIlIIIlIIll:
    IIlIIlIlIIlIllII[IIllllII:IIlllIIIIlIlIIII] = llIIlIIll[IllIIIllIIIIl:IlIIIlIIIlIIll]          
  elif lIIlIlllIl < IIlllIIIIlIlIIII:
    IIlIIlIlIIlIllII[IIllllII:IIlllIIIIlIlIIII] = llIIlIIll[lIIlIlllIl:IIlllIIIIlIlIIII]          
#
def lllllIlIlIlllllllI(IIllIlIIllIlIlII):
  IlIlIIIlIlIllI = len(IIllIlIIllIlIlII)
  IIIIllIIIIIIlllIl = math.ceil(math.log(IlIlIIIlIlIllI,2))
  llIIlIIll, lIIlllIlIllllI = IIllIlIIllIlIlII, [None] * IlIlIIIlIlIllI               
  for llllIllIIlllIIIllllI in (2**IIIlIllIlIIl for IIIlIllIlIIl in range(IIIIllIIIIIIlllIl)):   
    for IIllllll in range(0, IlIlIIIlIlIllI, 2 // llllIllIIlllIIIllllI):
      IllIIllIIllllIII(llIIlIIll, lIIlllIlIllllI, IIllllll, llllIllIIlllIIIllllI)
    llIIlIIll, lIIlllIlIllllI = lIIlllIlIllllI, llIIlIIll                 
  if IIllIlIIllIlIlII is not llIIlIIll:
    IIllIlIIllIlIlII[0:IlIlIIIlIlIllI] = llIIlIIll[0:IlIlIIIlIlIllI]                     
#
#Now the code should work correctly.
#
#
#