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

im = Image.open('road3_cropped.jpg')
#im.show()
im = im.convert('L')
im = np.array(im)

im = filters.gaussian(im,3)
im = filters.sobel(im)
im = threshold(im)
for i in range(6):
    for j in range(6):
        im = morphology.binary_dilation(im)
    im = morphology.skeletonize(im)
get(im).show()
