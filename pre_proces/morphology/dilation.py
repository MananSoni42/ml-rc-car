import sys
from PIL import Image
import numpy as np

def dilate(im,template):
    I = np.array(im)
    R = np.zeros(I.shape)

    T = np.array(template)
    m,n = T.shape

    for x in range(I.shape[0]):
        for y in range(I.shape[1]):
            mx = I[x,y] + T[0,0]
            for i in range(m):
                for j in range(n):
                    try:
                        if mx < I[x-i][y-j] + T[i,j]:
                            mx = I[x-i][y-j] + T[i,j]
                    except IndexError:
                        if mx < T[i,j]:
                            mx = T[i,j]
            R[x,y] = mx
    return R - 1

if __name__ == '__main__':
    im = Image.open(sys.argv[1])
    im = im.convert('L')
    im.show()

    T = [[1,1],[1,1]]

    dilated = dilate(im,T)

    new_im = Image.fromarray(255*dilated/np.max(dilated))
    new_im = new_im.convert('L')

    new_im.show()
