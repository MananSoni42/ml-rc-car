from skimage import filters,morphology,feature
from scipy import ndimage
from PIL import Image
import numpy as np

def threshold(im):
    thr = filters.threshold_otsu(im)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i,j] >= thr:
                im[i,j] = 1
            else:
                im[i,j] = 0
    return im

def get(im):
    return Image.fromarray(255*im/np.max(im))

def invert(im):
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i,j] == 1:
                im[i,j] = 0
            else:
                im[i,j] = 1

im = Image.open('road4_cropped.jpg')
im.show()
im = im.convert('L')
im = np.array(im)

im = filters.sobel_v(im)
im = threshold(im)
im = invert(im)

get(im).show()
