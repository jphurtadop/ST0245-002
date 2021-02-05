def subconjuntos(s):
    subconjuntosBase("", s)

def subconjuntosBase(base, t):
    if len(t) == 0:
        print(base)
    else:
        x = t[1:]
        subconjuntosBase(base+t[x],t[0:x])
        subconjuntosBase(base,t[x+1:])

print(subconjuntos("Santi"))
