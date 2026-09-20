# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:39:20 2026

@author: Sarah SM
"""
import cv2
import numpy as np
import math


# READ IMAGE

img = cv2.imread("images/kontras.jpeg", 0)

height, width = img.shape


# 1. NEGATIF

negative = np.zeros_like(img)

for i in range(height):
    for j in range(width):
        r = img[i, j]

        s = 255 - r

        negative[i, j] = s


# 2. LOGARITMIK

log_image = np.zeros_like(img)

for i in range(height):
    for j in range(width):
        r = int(img[i, j])

        s = (math.log(1 + r) / math.log(256)) * 255

        log_image[i, j] = int(s)


# 3. GAMMA

gamma = 2.0

gamma_image = np.zeros_like(img)

for i in range(height):
    for j in range(width):
        r = img[i, j] / 255

        s = (r ** gamma) * 255

        gamma_image[i, j] = int(s)


# 4. CONTRAST STRETCHING

r_min = img.min()
r_max = img.max()

contrast = np.zeros_like(img)

for i in range(height):
    for j in range(width):
        r = img[i, j]

        if r_max != r_min:
            s = ((r - r_min) / (r_max - r_min)) * 255
        else:
            s = r

        contrast[i, j] = int(s)


# 5. THRESHOLD

threshold = 128

threshold_image = np.zeros_like(img)

for i in range(height):
    for j in range(width):
        r = img[i, j]

        if r < threshold:
            s = 0
        else:
            s = 255

        threshold_image[i, j] = s


# 6. EKUALISASI HISTOGRAM

histogram = [0] * 256

for i in range(height):
    for j in range(width):
        pixel = img[i, j]

        histogram[pixel] += 1


cdf = [0] * 256

cdf[0] = histogram[0]

for i in range(1, 256):
    cdf[i] = cdf[i - 1] + histogram[i]


cdf_min = 0

for i in range(256):
    if cdf[i] > 0:
        cdf_min = cdf[i]
        break


equalized = np.zeros_like(img)

total_pixel = height * width

for i in range(height):
    for j in range(width):
        r = img[i, j]

        s = ((cdf[r] - cdf_min) /
             (total_pixel - cdf_min)) * 255

        equalized[i, j] = int(s)


# SHOW IMAGE

cv2.imshow("Kontras", img)

cv2.imshow("1. Negatif", negative)

cv2.imshow("2. Logaritmik", log_image)

cv2.imshow("3. Gamma", gamma_image)

cv2.imshow("4. Contrast Stretching", contrast)

cv2.imshow("5. Threshold", threshold_image)

cv2.imshow("6. Ekualisasi Histogram", equalized)


cv2.waitKey(0)
cv2.destroyAllWindows()