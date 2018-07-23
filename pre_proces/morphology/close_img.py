import sys
from PIL import Image
import numpy as np
from erosion import erode as E
from dilation import dilate as D

def CLOSE(im,T):
    return D(E(im,T),T)

if __name__ == '__main__':
    im = Image.open(sys.argv[1])
    im = im.convert('L')
    im.show()

    template = [[1],[1]]

    new_im = CLOSE  (im,template)

    new_im = Image.fromarray(255*new_im/np.max(new_im))
    new_im = new_im.convert('L')

    new_im.show()
