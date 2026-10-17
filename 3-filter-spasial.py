# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 21:40:45 2026

@author: Sarah SM
"""

import cv2
import numpy as np

# READ IMAGE

img = cv2.imread("images/terang.jpg", 0)

height, width = img.shape


# 1. BOX 3 x 3

box = np.zeros_like(img)

kernel_box = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
])

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        total = 0

        for m in range(3):
            for n in range(3):
                total += int(pad[i + m, j + n]) * kernel_box[m, n]

        box[i, j] = int(total / 9)


# 2. GAUSSIAN 3 x 3

gaussian = np.zeros_like(img)

kernel_gaussian = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
])

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        total = 0

        for m in range(3):
            for n in range(3):
                total += int(pad[i + m, j + n]) * kernel_gaussian[m, n]

        gaussian[i, j] = int(total / 16)


# 3. MEDIAN

median = np.zeros_like(img)

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        nilai = []

        for m in range(3):
            for n in range(3):
                nilai.append(int(pad[i + m, j + n]))

        nilai.sort()

        median[i, j] = nilai[4]


# 4. LAPLACIAN 4

laplacian4 = np.zeros_like(img)

kernel_lap4 = np.array([
    [0, -1,  0],
    [-1, 4, -1],
    [0, -1,  0]
])

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        total = 0

        for m in range(3):
            for n in range(3):
                total += int(pad[i + m, j + n]) * kernel_lap4[m, n]

        total = abs(total)

        if total > 255:
            total = 255

        laplacian4[i, j] = total

 
# 5. LAPLACIAN 8

laplacian8 = np.zeros_like(img)

kernel_lap8 = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        total = 0

        for m in range(3):
            for n in range(3):
                total += int(pad[i + m, j + n]) * kernel_lap8[m, n]

        total = abs(total)

        if total > 255:
            total = 255

        laplacian8[i, j] = total


# 6. PENAJAM

penajam = np.zeros_like(img)

kernel_penajam = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        total = 0

        for m in range(3):
            for n in range(3):
                total += int(pad[i + m, j + n]) * kernel_penajam[m, n]

        if total < 0:
            total = 0

        if total > 255:
            total = 255

        penajam[i, j] = total


# 7. SOBEL X

sobel_x = np.zeros_like(img)

kernel_sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        total = 0

        for m in range(3):
            for n in range(3):
                total += int(pad[i + m, j + n]) * kernel_sobel_x[m, n]

        total = abs(total)

        if total > 255:
            total = 255

        sobel_x[i, j] = total


# 8. SOBEL Y

sobel_y = np.zeros_like(img)

kernel_sobel_y = np.array([
    [-1, -2, -1],
    [0,  0,  0],
    [1,  2,  1]
])

pad = np.pad(img, ((1, 1), (1, 1)), mode='edge')

for i in range(height):
    for j in range(width):

        total = 0

        for m in range(3):
            for n in range(3):
                total += int(pad[i + m, j + n]) * kernel_sobel_y[m, n]

        total = abs(total)

        if total > 255:
            total = 255

        sobel_y[i, j] = total


# SHOW IMAGE

cv2.imshow("Asli", img)

cv2.imshow("1. Box 3 x 3", box)
cv2.imshow("2. Gaussian 3 x 3", gaussian)
cv2.imshow("3. Median", median)
cv2.imshow("4. Laplacian 4", laplacian4)
cv2.imshow("5. Laplacian 8", laplacian8)
cv2.imshow("6. Penajam", penajam)
cv2.imshow("7. Sobel X", sobel_x)
cv2.imshow("8. Sobel Y", sobel_y)

cv2.waitKey(0)
cv2.destroyAllWindows()