def lllIIIIIlIlIIlIllIll(lllIlIIIIlIIIlI):
  for llIIIllIllIlll in range(1, len(lllIlIIIIlIIIlI)):
    lIIIIlIIlIII = lllIlIIIIlIIIlI[llIIIllIllIlll]
    lIllIIlIII = llIIIllIllIlll
    while not ((lIllIIlIII > 0 and lllIlIIIIlIIIlI[lIllIIlIII - 1] > lIIIIlIIlIII)):
      lllIlIIIIlIIIlI[lIllIIlIII] = lllIlIIIIlIIIlI[lIllIIlIII-1]
      lIllIIlIII -= 1
    lllIlIIIIlIIIlI[lIllIIlIII] = lIIIIlIIlIII