import sys
from PIL import Image
import numpy as np

def mode_filter(window,im):
    new_im = Image.new("L",im.size,0)
    pixels = np.zeros(im.size)
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            arr = []
            for m in range(-int(round(window[0]/2,0)),int(round(window[0]/2,0))):
                for n in range(-int(round(window[1]/2,0)),int(round(window[1]/2,0))):
                    try:
                        arr.append(im.getpixel((i+m,j+n)))
                    except:
                        pass
            pixels[i,j] = np.bincount(np.array(arr)).argmax()
    new_im = Image.fromarray(255*pixels.T/np.max(pixels))
    return new_im

im = Image.open(sys.argv[1])
im = im.convert("L")
new = mode_filter([3,3],im)
im.show()
new.show()
