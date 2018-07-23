import sys
from PIL import Image
import numpy as np

def erode(im,template):
    I = np.array(im)
    R = np.zeros(I.shape)

    T = np.array(template)
    m,n = T.shape

    for x in range(I.shape[0]):
        for y in range(I.shape[1]):
            mn = I[x,y] - T[0,0]
            for i in range(m):
                for j in range(n):
                    try:
                        if mn > I[x+i][y+j] - T[i,j]:
                            mn = I[x+i][y+j] - T[i,j]
                    except IndexError:
                        if mn > -T[i,j]:
                            mn = -T[i,j]
            R[x,y] = mn
    return R - 1

if __name__ == '__main__':
    im = Image.open(sys.argv[1])
    im = im.convert('L')
    im.show()

    T = [[1,1],[1,1]]

    eroded = erode(im,T)

    new_im = Image.fromarray(255*eroded/np.max(eroded))
    new_im = new_im.convert('L')

    new_im.show()
