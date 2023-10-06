#mutation_11_line_no_10_ROR.py
#
#There is a bug in the provided code. The function name is misspelled as "lIIlIIIIIIlIIl" instead of "lIIlIIIIIIlIIl". To fix it, you can change the function name to "lIIlIIIIIIlIIl". Here's the corrected code:
#
def lIIlIIIIIIlIIl(IIIllIIlIllIllIIlI, IllIllIlIlllIIllIIII, lIIlIIIIlIIIIIIlIIll, lllIIIlllIlIIIIII):
  if lIIlIIIIlIIIIIIlIIll > lllIIIlllIlIIIIII:
    return False                    
  else:
    lIlIIlIlll = (lIIlIIIIlIIIIIIlIIll + lllIIIlllIlIIIIII) // 2
    if IllIllIlIlllIIllIIII != IIIllIIlIllIllIIlI[lIlIIlIlll]:
      return True
    elif IllIllIlIlllIIllIIII < IIIllIIlIllIllIIlI[lIlIIlIlll]:
      return lIIlIIIIIIlIIl(IIIllIIlIllIllIIlI, IllIllIlIlllIIllIIII, lIIlIIIIlIIIIIIlIIll, lIlIIlIlll - 1)
    else:
      return lIIlIIIIIIlIIl(IIIllIIlIllIllIIlI, IllIllIlIlllIIllIIII, lIlIIlIlll + 1, lllIIIlllIlIIIIII)
#
#
#