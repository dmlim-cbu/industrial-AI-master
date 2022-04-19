import numpy as np
import cv2

keyin = input("[영상셋 2장] boat(1), budapest(2), newpaper(3), s(4) 4개의 영상셋 중 하니를 선택해 주세요. : ")

if keyin == "1":
    image0 = cv2.imread('stitching/boat1.jpg', cv2.IMREAD_COLOR)
    image0 = cv2.resize(image0, None, fx=0.2, fy=0.2)
    image1 = cv2.imread('stitching/boat2.jpg', cv2.IMREAD_COLOR)
    image1 = cv2.resize(image1, None, fx=0.2, fy=0.2)
elif keyin == "2":
    image0 = cv2.imread('stitching/budapest1.jpg', cv2.IMREAD_COLOR)
    image0 = cv2.resize(image0, None, fx=0.5, fy=0.5)
    image1 = cv2.imread('stitching/budapest2.jpg', cv2.IMREAD_COLOR)
    image1 = cv2.resize(image1, None, fx=0.5, fy=0.5)
elif keyin == "3":
    image0 = cv2.imread('stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
    image0 = cv2.resize(image0, None, fx=0.5, fy=0.5)
    image1 = cv2.imread('stitching/newspaper2.jpg', cv2.IMREAD_COLOR)
    image1 = cv2.resize(image1, None, fx=0.5, fy=0.5)
elif keyin == "4":
    image0 = cv2.imread('stitching/s1.jpg', cv2.IMREAD_COLOR)
    image0 = cv2.resize(image0, None, fx=0.5, fy=0.5)
    image1 = cv2.imread('stitching/s2.jpg', cv2.IMREAD_COLOR)
    image1 = cv2.resize(image1, None, fx=0.5, fy=0.5)

gray0 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kps0, fea0 = sift.detectAndCompute(gray0,None)
kps1, fea1 = sift.detectAndCompute(gray1,None)
img_draw0 = cv2.drawKeypoints(image0, kps0, None, \
             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT 0', img_draw0)
img_draw1 = cv2.drawKeypoints(image1, kps1, None, \
             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT 1', img_draw1)

matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = matcher.match(fea0, fea1)
#matches = sorted(matches, key = lambda x:x.distance)
pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1,2)
pts1 = np.float32([kps1[m.trainIdx].pt for m in matches]).reshape(-1,2)
H, mask = cv2.findHomography(pts0, pts1, cv2.RANSAC, 3.0)

dbg_img = cv2.drawMatches(gray0, kps0, gray1, kps1, matches[:50], gray1, flags=2)
cv2.imshow('SIFT all matches', dbg_img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

orb = cv2.ORB_create(100)
kps0, fea0 = orb.detectAndCompute(image0, None)
kps1, fea1 = orb.detectAndCompute(image1, None)
img_draw0 = cv2.drawKeypoints(image0, kps0, None, \
             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('ORB 0', img_draw0)
img_draw1 = cv2.drawKeypoints(image1, kps1, None, \
             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('ORB 1', img_draw1)

matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(fea0, fea1)
pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1,2)
pts1 = np.float32([kps1[m.trainIdx].pt for m in matches]).reshape(-1,2)
H, mask = cv2.findHomography(pts0, pts1, cv2.RANSAC, 3.0)

dbg_img = cv2.drawMatches(image0, kps0, image1, kps1, matches[:50], gray1, flags=2)
cv2.imshow('ORB all matches', dbg_img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

surf = cv2.xfeatures2d.SURF_create()
kps0, fea0 = surf.detectAndCompute(gray0,None)
kps1, fea1 = surf.detectAndCompute(gray1,None)
img_draw0 = cv2.drawKeypoints(image0, kps0, None, \
             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF 0', img_draw0)
img_draw1 = cv2.drawKeypoints(image1, kps1, None, \
             flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SURF 1', img_draw1)

matcher = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = matcher.match(fea0, fea1)
#matches = sorted(matches, key = lambda x:x.distance)
pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1,2)
pts1 = np.float32([kps1[m.trainIdx].pt for m in matches]).reshape(-1,2)
H, mask = cv2.findHomography(pts0, pts1, cv2.RANSAC, 3.0)

dbg_img = cv2.drawMatches(image0, kps0, image1, kps1, matches[:50], gray1, flags=2)
cv2.imshow('SURF matches', dbg_img)

if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
