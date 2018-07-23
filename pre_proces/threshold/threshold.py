#!/usr/bin/python3

import sys
from PIL import Image

im = Image.open(sys.argv[1])
im = im.convert('L')
print(im.size)
def threshold(G,im):
    P = im.size[0]*im.size[1]

    f = []
    F = []
    gf = []
    GF = []
    m = []
    T = []

    for i in range(G):
        f.append(1)
        F.append(0)
        gf.append(0)
        GF.append(0)
        m.append(0)
        T.append(0)

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            f[im.getpixel((i,j))]+=1

    F[0] = f[0]
    gf[0] = 0
    for i in range(1,G):
        F[i] = F[i-1] + f[i]
        gf[i] = i*f[i]

    GF[0] = 0
    for i in range(1,G):
        GF[i] = GF[i-1] + gf[i]

    for i in range(G):
        try:
            m[i] = GF[i]/F[i]
        except:
            try:
                m[i] = m[i-1]
            except:
                pass

    for i in range(G):
        try:
            T[i] = (F[i]/(P-F[i]))*(m[i]-m[G-1])**2
        except:
            try:
                T[i] = T[i-1]
            except:
                pass
    return T.index(max(T))-1

G = 256
thr = threshold(G,im)

im.show()

for i in range(im.size[0]):
    for j in range(im.size[1]):
        if im.getpixel((i,j)) >= thr:
            im.putpixel((i,j),G-1)
        else:
            im.putpixel((i,j),0)

im.show()
