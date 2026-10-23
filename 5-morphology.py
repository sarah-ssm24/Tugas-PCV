# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 20:30:21 2026

@author: Sarah SM
"""

import cv2
import numpy as np

# READ IMAGE

img = cv2.imread("images/terang.jpg", 0)

_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

height, width = binary.shape

# Struktur Element 3 x 3
kernel = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
], dtype=np.uint8)

pad_h, pad_w = 1, 1


# 1. EROSI

erosi = np.zeros_like(binary)
pad = np.pad(binary, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

for i in range(height):
    for j in range(width):

        fit = True

        for m in range(3):
            for n in range(3):
                if kernel[m, n] == 1 and pad[i + m, j + n] != 255:
                    fit = False
                    break
            if not fit:
                break
        
        if fit:
            erosi[i, j] = 255
        else:
            erosi[i, j] = 0


# 2. DILASI

dilasi = np.zeros_like(binary)

for i in range(height):
    for j in range(width):

        hit = False

        for m in range(3):
            for n in range(3):
                if kernel[m, n] == 1 and pad[i + m, j + n] == 255:
                    hit = True
                    break
            if hit:
                break
        
        if hit:
            dilasi[i, j] = 255
        else:
            dilasi[i, j] = 0


# 3. OPENING (Erosi diikuti Dilasi)

opening = np.zeros_like(binary)
pad_erosi = np.pad(erosi, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

for i in range(height):
    for j in range(width):

        hit = False

        for m in range(3):
            for n in range(3):
                if kernel[m, n] == 1 and pad_erosi[i + m, j + n] == 255:
                    hit = True
                    break
            if hit:
                break
        
        if hit:
            opening[i, j] = 255
        else:
            opening[i, j] = 0


# 4. CLOSING (Dilasi diikuti Erosi)

closing = np.zeros_like(binary)
pad_dilasi = np.pad(dilasi, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

for i in range(height):
    for j in range(width):

        fit = True

        for m in range(3):
            for n in range(3):
                if kernel[m, n] == 1 and pad_dilasi[i + m, j + n] != 255:
                    fit = False
                    break
            if not fit:
                break
        
        if fit:
            closing[i, j] = 255
        else:
            closing[i, j] = 0


# SHOW IMAGE

cv2.imshow("Asli (Biner)", binary)

cv2.imshow("1. Erosi", erosi)
cv2.imshow("2. Dilasi", dilasi)
cv2.imshow("3. Opening", opening)
cv2.imshow("4. Closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()