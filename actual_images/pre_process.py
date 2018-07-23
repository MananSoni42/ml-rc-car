#!/usr/bin/python3

import sys
from skimage import filters,morphology,feature
from scipy import ndimage
from PIL import Image
import numpy as np
import math

def threshold(im):
    thr = filters.threshold_otsu(im)
    im = 1*(im >= thr)
    return im

def get(im):
    return Image.fromarray(255*im/np.max(im))

def pearson_correlation(arr):
    pts = np.nonzero(arr)

    if len(pts[0]) < 4:
        return 1

    x = pts[1]
    av_x = np.mean(x)
    y = pts[0]
    av_y = np.mean(y)

    r = np.sum( (x-av_x)*(y-av_y) ) / (np.sqrt( np.sum( (x-av_x)*(x-av_x) )*np.sum( (x-av_x)*(x-av_x) ) ))
    return abs(r)

def remove_small(im,window=[5,5]):
    num_pts = window[0]*window[1]
    for i in range(0,im.shape[0]-window[0],window[0]):
        for j in range(0,im.shape[1]-window[1],window[1]):
            pts = np.nonzero(im[i:i+window[0],j:j+window[1]])
            if len(pts[0]) < num_pts*0.15:
                im[i:i+window[0],j:j+window[1]] = 0
    return im

def improve_cor(im,window=[10,10]):
    for i in range(0,im.shape[0]-window[0],window[0]):
        for j in range(0,im.shape[1]-window[1],window[1]):
            coeff = pearson_correlation(im[i:i+window[0],j:j+window[1]])
            if coeff < 0.2:
                im[i:i+window[0],j:j+window[1]] = 0
    return im

def fix_holes(im):
    for i in range(im.shape[1]):
        lst = [j for j in range(im.shape[0]) if im[j,i] == 1]
        if len(lst) == 2:
            im[lst[0],i] = 0
            im[lst[1],i] = 0
            im[int(round((lst[0]+lst[1])/2,0)),i] = 1

        if len(lst) > 2:
            sublst = [ lst[j]-lst[j-1] for j in range(1,len(lst)) ]
            ind = sublst.index(min(sublst))
            im[lst[ind],i] = 0
            im[lst[ind-1],i] = 0
            im[int(round((lst[ind]+lst[ind-1])/2,0)),i] = 1

    return im

def remove_hor(im):
    for i in range(1,im.shape[0]-1):
        lst = [j for j in range(im.shape[1]-1) if im[i,j] == 1 and (im[i,j+1]==1 or im[i-1,j+1]==1 or im[i+1,j+1]==1)]
        if len(lst) > im.shape[1]/20:
            for j in lst:
                im[i,j] = 0
    return im

in_name = f'road{sys.argv[1]}_cropped.jpg'
out_name = f'road{sys.argv[1]}_final.jpg'

im = Image.open(in_name)
im.show()
im = im.convert('L')
im = np.array(im)

im = filters.gaussian(im,3)
im = filters.sobel(im)
im = threshold(im)
for j in range(5):
    im = morphology.binary_dilation(im)
im = 1*morphology.skeletonize(im)

#im = remove_hor(im)
#im = fix_holes(im)
im = improve_cor(im)
im = remove_small(im)

for j in range(5):
    im = morphology.binary_dilation(im)
im = 1*morphology.skeletonize(im)

try:
    sys.argv[2]
    get(im).convert('RGB').save(out_name)
except:
    get(im).show()
