import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('peppers.png', 0).astype(np.float32) / 255

radius = np.int(input("radius = "))
center = image.shape[0]//2
circle_img = cv2.circle(image, (center, center), radius, 0, 5)

fft = cv2.dft(circle_img, flags = cv2.DFT_COMPLEX_OUTPUT)
fft_shift = np.fft.fftshift(fft, axes=[0,1])
sz = 25

fft = fft * radius

mask = np.zeros(fft.shape, np.uint8)
mask[image.shape[0]//2-sz:image.shape[0]//2+sz, image.shape[1]//2-sz:image.shape[1]//2+sz, :] = 1

frequancy = input("frequancy 'HIGH' or 'LOW' = ").upper()

if frequancy == "HIGH":
    fft_shift *= 1 - mask
    frequancy = "HIGH"
elif frequancy == "LOW":
    fft_shift *= mask
    frequancy = "LOW"

fft = np.fft.ifftshift(fft_shift, axes=[0,1])
filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
mask_new = np.dstack((mask, np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)))

image = cv2.imread('peppers.png', 0).astype(np.float32) / 255

plt.figure()
plt.subplot(131)
plt.axis('off')
plt.title('original')
plt.imshow(image, cmap='gray')

plt.subplot(132)
plt.axis('off')
plt.title('circle')
plt.imshow(circle_img, cmap='gray')

plt.subplot(133)
plt.axis('off')
plt.title(frequancy + ' frequancy')
plt.imshow(filtered, cmap='gray')

plt.tight_layout()
plt.show()