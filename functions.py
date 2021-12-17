from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread
from matplotlib import pyplot as plt 
plt.rcParams["figure.figsize"] = (20,30)


def find_stars(file):

    file = glob.glob('{}.jpeg'.format(file))[0]

    im = imread(file, as_gray=True)

    plt.imshow(im, cmap=plt.get_cmap('gray'))

    plt.show()

    blobs_log = blob_log(im, max_sigma=10, min_sigma=1, threshold=.09)

    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)

    numrows = len(blobs_log)

    print(numrows)

    fig, ax = plt.subplots(1,1)

    plt.imshow(im, cmap= plt.get_cmap('gray'))

    for blob in blobs_log:

        y, x, z = blob

        c = plt.Circle((x, y), z+5, color = 'lime', linewidth = 1, fill = False)

        ax.add_patch(c)