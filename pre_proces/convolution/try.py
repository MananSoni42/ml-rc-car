import sys
from PIL import Image
import numpy as np

def convolve(T,im):
    arr = np.array(im)
    t = np.array(T)
    l = arr.shape[0] - t.shape[0] + 1
    b = arr.shape[1] - t.shape[1] + 1
    new_arr = np.zeros(arr.shape)

    for i in range(l):
        for j in range(b):
            new_arr[i][j] = np.sum(t*arr[i:i+t.shape[0],j:j+t.shape[1]])
    return new_arr

im = Image.open(sys.argv[1])
im = im.convert('L')
T1 = [[-1,1],[-1,1]]
T2 = [[-1,-1],[1,1]]
new1 = convolve(T1,im)
new2 = convolve(T2,im)
new = new1 + new2
new = Image.fromarray(255*new/np.max(new))
new1 = Image.fromarray(255*new1/np.max(new1))
new2 = Image.fromarray(255*new2/np.max(new2))

#print('Convolution:\n',np.array(T))
im.show()
new1.show()
new2.show()
new.show()
