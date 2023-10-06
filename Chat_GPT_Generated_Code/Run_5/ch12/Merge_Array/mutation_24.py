#mutation_24_line_no_20_SIR.py
#
#There is a bug in the provided code. The bug is in the line `IIIIIlIlIIlllI(lllIllIIl[:llllIllll])`. This line should be `IIIIIlIlIIlllI(lllIllIIl[lllllIlIlIIllIIlIllI:])` instead. 
#
#Here is the corrected code:
#
def lllIIIlIllIIlIII(llIlIIllIIlIlIllll, IIIIIlII, lllIllIIl):
  lIlllIllllIIIIIIll = lllllIIIIlIIlllI = 0
  while lIlllIllllIIIIIIll + lllllIIIIlIIlllI < len(lllIllIIl):
    if lllllIIIIlIIlllI == len(IIIIIlII) or (lIlllIllllIIIIIIll < len(llIlIIllIIlIlIllll) and llIlIIllIIlIlIllll[lIlllIllllIIIIIIll] < IIIIIlII[lllllIIIIlIIlllI]):
      lllIllIIl[lIlllIllllIIIIIIll+lllllIIIIlIIlllI] = llIlIIllIIlIlIllll[lIlllIllllIIIIIIll]      
      lIlllIllllIIIIIIll += 1
    else:
      lllIllIIl[lIlllIllllIIIIIIll+lllllIIIIlIIlllI] = IIIIIlII[lllllIIIIlIIlllI]      
      lllllIIIIlIIlllI += 1
def IIIIIIlIlIIlllI(lllIllIIl):
  llllIllll = len(lllIllIIl)
  if llllIllll < 2:
    return                
  lllllIlIlIIllIIlIllI = llllIllll // 2
  llIlIIllIIlIlIllll = lllIllIIl[0:lllllIlIlIIllIIlIllI]           
  IIIIIlII = lllIllIIl[lllllIlIlIIllIIlIllI:]  # Corrected line
  IIIIIIlIlIIlllI(llIlIIllIIlIlIllll)          
  IIIIIIlIlIIlllI(IIIIIlII)          
  lllIIIlIllIIlIII(llIlIIllIIlIlIllll, IIIIIlII, lllIllIIl)
#
#
#