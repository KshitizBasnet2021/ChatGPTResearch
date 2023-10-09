def IIIllllIlIllIIII(llIIllIllIl):
    lIIllIIlI = [IlllIIIIllIIllI for IlllIIIIllIIllI in llIIllIllIl if not IlllIIIIllIIllI.incoming_nodes]
    for IlllIIIIllIIllI in lIIllIIlI:
        for llllllllIllllIlIII in IlllIIIIllIIllI.outgoing_nodes:
            if set(lIIllIIlI).issuperset(llllllllIllllIlIII.outgoing_nodes) and llllllllIllllIlIII not in lIIllIIlI:
                lIIllIIlI.append(llllllllIllllIlIII)
    return lIIllIIlI