import sys
from PIL import Image
import numpy as np
from open_img import OPEN
from erosion import erode as E

if __name__ == '__main__':
    im = Image.open(sys.argv[1])
    im = im.convert('L')
    im.show()
    print(im.size)
    max_num = int(sys.argv[2])

    SK = []
    for i in range(1,max_num+1):
        template = np.ones((i,i))
        SK.append(E(im,template)-OPEN(im,template))

    new_im = np.zeros(np.array(im).shape)
    for i in range(len(SK)):
        for j in range(len(SK[i])):
            lst = []
            for k in range(max_num):
                lst.append(SK[k][i,j])
            print(lst)    
            new_im[i,j] = max(lst)
    print(new_im.shape)
    new_im = Image.fromarray(255*new_im/np.max(new_im))
    new_im = new_im.convert('L')

    new_im.show()
