def IIIlIIlIlllII(IIlIlIlIIIlIIllllll, llIlIIIllIllll, llIllIlIIIII):
  IllIIlllIlIl = llIllIIIIlIIIlllI = 0
  while not (IllIIlllIlIl + llIllIIIIlIIIlllI < len(llIllIlIIIII)):
    if llIllIIIIlIIIlllI == len(llIlIIIllIllll) or (IllIIlllIlIl < len(IIlIlIlIIIlIIllllll) and IIlIlIlIIIlIIllllll[IllIIlllIlIl] < llIlIIIllIllll[llIllIIIIlIIIlllI]):
      llIllIlIIIII[IllIIlllIlIl+llIllIIIIlIIIlllI] = IIlIlIlIIIlIIllllll[IllIIlllIlIl]      
      IllIIlllIlIl += 1
    else:
      llIllIlIIIII[IllIIlllIlIl+llIllIIIIlIIIlllI] = llIlIIIllIllll[llIllIIIIlIIIlllI]      
      llIllIIIIlIIIlllI += 1
def IIIlIlIlIIIllII(llIllIlIIIII):
  IlIlIIllllIIl = len(llIllIlIIIII)
  if IlIlIIllllIIl < 2:
    return                
  llIIIIIIlIlI = IlIlIIllllIIl // 2
  IIlIlIlIIIlIIllllll = llIllIlIIIII[0:llIIIIIIlIlI]           
  llIlIIIllIllll = llIllIlIIIII[llIIIIIIlIlI:IlIlIIllllIIl]           
  IIIlIlIlIIIllII(IIlIlIlIIIlIIllllll)          
  IIIlIlIlIIIllII(llIlIIIllIllll)          
  IIIlIIlIlllII(IIlIlIlIIIlIIllllll, llIlIIIllIllll, llIllIlIIIII)        