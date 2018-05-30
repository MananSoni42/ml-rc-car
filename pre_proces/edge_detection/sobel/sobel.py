import sys
from PIL import Image
from threshold import threshold
from convolution import convolve
import numpy as np

x_dir = [[-1,0,1],[-2,0,2],[-1,0,1]]
y_dir = [[1,2,1],[0,0,0],[-1,-2,-1]]

im = Image.open(sys.argv[1])
im = im.convert("L")

im.show()

A = convolve(x_dir,im)
B = convolve(y_dir,im)

conv_im = B
#conv_im = abs(A) + abs(B)
conv_im = Image.fromarray(255*conv_im/np.max(conv_im))

G = 256

thr = threshold(G,conv_im)

for i in range(conv_im.size[0]):
    for j in range(conv_im.size[1]):
        if conv_im.getpixel((i,j)) >= thr:
            conv_im.putpixel((i,j),G-1)
        else:
            conv_im.putpixel((i,j),0)

conv_im = conv_im.convert('RGB')
conv_im.save('final1.png')
