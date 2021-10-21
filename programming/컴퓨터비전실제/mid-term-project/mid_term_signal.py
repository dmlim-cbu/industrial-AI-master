import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randint

keyin = input("r, g, y 신호등 이미지를 선택하세요. : ")

if keyin == "r":
    img_org = cv2.imread("signal_r.jpg")
    image = cv2.imread("signal_r.jpg", 0)

elif keyin == "g":
    img_org = cv2.imread("signal_g.jpg", cv2.IMREAD_COLOR)
    image = cv2.imread("signal_g.jpg", 0)

elif keyin == "y":
    img_org = cv2.imread("signal_y.jpg", cv2.IMREAD_COLOR)
    image = cv2.imread("signal_y.jpg", 0)

cv2.imshow('Original Image', img_org)
cv2.waitKey()
cv2.destroyAllWindows()

dx = cv2.Sobel(image, cv2.CV_32F, 1, 0)

show_img = np.copy(img_org)

mouse_pressed = False
y = x = w = h = 0

def mouse_callback(event, _x, _y, flags, param):
    global show_img, x, y, w, h, mouse_pressed

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        x, y = _x, _y
        show_img = np.copy(img_org)

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            show_img = np.copy(img_org)
            cv2.rectangle(show_img, (x, y), (_x, _y), (0, 255, 0), 3)

    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False
        w, h = _x - x, _y - y

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', show_img)
    k = cv2.waitKey(1)

    if k == ord('a') and not mouse_pressed:
        if w * h > 0:
            break

cv2.destroyAllWindows()

labels = np.zeros(img_org.shape[:2], np.uint8)
labels, bgdModel, fgdModel = cv2.grabCut(img_org, labels,
     (x, y, w, h), None, None, 5, cv2.GC_INIT_WITH_RECT)

show_img = np.copy(img_org)
show_img[(labels == cv2.GC_PR_BGD) | (labels == cv2.GC_BGD)] //= 3

cv2.imshow('image', show_img)
cv2.waitKey()
cv2.destroyAllWindows()

seg_img = np.copy(show_img)

#/////////////////////////////////////////////////////////////////
seeds = np.full(show_img.shape[0:2], 0, np.int32)
segmentation = np.full(show_img.shape, 0, np.uint8)

m_seeds = 9

colors = []
for m in range(m_seeds):
    colors.append((255 * m / m_seeds, randint(0, 255), randint(0, 255)))

mouse_pressed = False
current_seed = 1
seeds_updated = False

def mouse_callback(event, x, y, flags, param):
    global mouse_pressed, seeds_updated

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_pressed = True
        cv2.circle(seeds, (x, y), 5, (current_seed), cv2.FILLED)
        cv2.circle(seg_img, (x, y), 5, colors[current_seed - 1], cv2.FILLED)
        seeds_updated = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_pressed:
            cv2.circle(seeds, (x, y), 5, (current_seed), cv2.FILLED)
            cv2.circle(seg_img, (x, y), 5, colors[current_seed - 1], cv2.FILLED)
            seeds_updated = True
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_pressed = False

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('segmentation', segmentation)
    cv2.imshow('image', seg_img)

    k = cv2.waitKey(1)

    if k == 27:

        break
    elif k == ord('c'):
        seg_img = np.copy(show_img)
        seeds = np.full(show_img.shape[0:2], 0, np.int32)
        segmentation = np.full(show_img.shape, 0, np.uint8)

    elif k > 0 and chr(k).isdigit():
        m = int(chr(k))
        if 1 <= m <= m_seeds and not mouse_pressed:
            current_seed = m

    if seeds_updated and not mouse_pressed:
        seeds_copy = np.copy(seeds)
        cv2.watershed(show_img, seeds_copy)
        segmentation = np.full(show_img.shape, 0, np.uint8)

        for m in range(m_seeds):
            segmentation[seeds_copy == (m + 1)] = colors[m]

        seeds_updated = False

cv2.destroyAllWindows()

plt.figure(figsize=(10,5))
plt.subplot(131)
plt.axis('off')
plt.title('sobel')
plt.imshow(dx, cmap='gray')
plt.subplot(132)
plt.axis('off')
plt.title('grabCut')
plt.imshow(show_img[:, :, [2, 1, 0]])
plt.subplot(133)
plt.axis('off')
plt.title('segmentation')
plt.imshow(segmentation[:, :, [2, 1, 0]])

plt.tight_layout()
plt.show()
