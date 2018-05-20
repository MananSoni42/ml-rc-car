import sys
from PIL import Image
import numpy as np

def moravec(im):
    new_im = Image.new("L",im.size,0)
    pixels = np.zeros(im.size)
    var = np.zeros(im.size)
    cornerness = np.zeros(im.size)
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            for k in range(-1,1):
                for l in range(-1,1):
                    try:
                        var[i,j]+= (im.getpixel((i,j))-im.getpixel((i+k,j+l)))**2
                    except:
                        pass

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            arr = []
            for k in range(-1,1):
                for l in range(-1,1):
                    try:
                        arr.append(var[i+k][j+l])
                    except:
                        pass
            cornerness[i,j] = min(arr)

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            arr = []
            for k in range(-1,1):
                for l in range(-1,1):
                    if k is 0 and l is 0:
                        continue
                    try:
                        arr.append(cornerness[i+k][j+l])
                    except:
                        pass
            if im.getpixel((i,j)) <= max(arr):
                pixels[i,j] = 0
            else:
                pixels[i,j] = 255

    new_im = Image.fromarray(255*pixels.T/np.max(pixels))
    return new_im

im = Image.open(sys.argv[1])
im = im.convert("L")
new = moravec(im)
im.show()
new.show()
