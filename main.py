import cv2
import numpy
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread('Photo.jpg')

width = int(image.shape[1] * 50 / 100)
height = int(image.shape[0] * 50 / 100)

dsize = (width, height)
image = cv2.resize(image, dsize)

boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128])
]

for (lower, upper) in boundaries:
    lower = numpy.array(lower, dtype="uint8")
    upper = numpy.array(upper, dtype="uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    cv2.imshow("images", numpy.hstack([image, output]))
    cv2.waitKey(0)