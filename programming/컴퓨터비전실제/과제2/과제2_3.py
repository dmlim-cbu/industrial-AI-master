import cv2
import numpy as np

images = []
images.append(cv2.imread('stitching/boat1.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('stitching/boat2.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('stitching/boat3.jpg', cv2.IMREAD_COLOR))
images.append(cv2.imread('stitching/boat4.jpg', cv2.IMREAD_COLOR))

stitcher = cv2.createStitcher()
ret, pano = stitcher.stitch(images)

if ret == cv2.Stitcher_OK:
    pano = cv2.resize(pano, dsize=(0,0), fx=0.2, fy=0.2)
    cv2.imshow('panorama', pano)
    cv2.waitKey()

    cv2.destroyAllWindows()
else:
    print('Error during stiching')