# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:28:59 2026

@author: Sarah SM
"""

import cv2
import numpy as np

# READ IMAGE (Warna RGB/BGR)
img = cv2.imread("images/terang.jpg")

height, width, _ = img.shape


# 1. KONVERSI RGB (Kanal B, G, R Terpisah)

b_channel, g_channel, r_channel = cv2.split(img)

img_r = np.zeros_like(img)
img_r[:, :, 2] = r_channel

img_g = np.zeros_like(img)
img_g[:, :, 1] = g_channel

img_b = np.zeros_like(img)
img_b[:, :, 0] = b_channel


# 2. KONVERSI CMYK

c_img = np.zeros((height, width), dtype=np.uint8)
m_img = np.zeros((height, width), dtype=np.uint8)
y_img = np.zeros((height, width), dtype=np.uint8)
k_img = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        b = img[i, j, 0] / 255.0
        g = img[i, j, 1] / 255.0
        r = img[i, j, 2] / 255.0

        k = 1.0 - max(r, g, b)
        if k == 1.0:
            c = 0.0
            m = 0.0
            y = 0.0
        else:
            c = (1.0 - r - k) / (1.0 - k)
            m = (1.0 - g - k) / (1.0 - k)
            y = (1.0 - b - k) / (1.0 - k)

        c_img[i, j] = int(c * 255)
        m_img[i, j] = int(m * 255)
        y_img[i, j] = int(y * 255)
        k_img[i, j] = int(k * 255)


# 3. KONVERSI HSI

h_hsi = np.zeros((height, width), dtype=np.uint8)
s_hsi = np.zeros((height, width), dtype=np.uint8)
i_hsi = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        b = float(img[i, j, 0])
        g = float(img[i, j, 1])
        r = float(img[i, j, 2])

        total = r + g + b
        if total == 0:
            s = 0
            h = 0
        else:
            s = 1.0 - (3.0 / total) * min(r, g, b)
            
            num = 0.5 * ((r - g) + (r - b))
            den = np.sqrt((r - g)**2 + (r - b) * (g - b))
            
            if den == 0:
                h = 0
            else:
                val = np.clip(num / den, -1.0, 1.0)
                theta = np.arccos(val) * (180.0 / np.pi)
                if b > g:
                    h = 360.0 - theta
                else:
                    h = theta

        h_hsi[i, j] = int((h / 360.0) * 255)
        s_hsi[i, j] = int(s * 255)
        i_hsi[i, j] = int(total / 3.0)


# 4. KONVERSI HSV

h_hsv = np.zeros((height, width), dtype=np.uint8)
s_hsv = np.zeros((height, width), dtype=np.uint8)
v_hsv = np.zeros((height, width), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        b = img[i, j, 0] / 255.0
        g = img[i, j, 1] / 255.0
        r = img[i, j, 2] / 255.0

        v = max(r, g, b)
        c_min = min(r, g, b)
        diff = v - c_min

        if v == 0:
            s = 0
        else:
            s = diff / v

        if diff == 0:
            h = 0
        elif v == r:
            h = 60.0 * (((g - b) / diff) % 6)
        elif v == g:
            h = 60.0 * (((b - r) / diff) + 2)
        elif v == b:
            h = 60.0 * (((r - g) / diff) + 4)

        h_hsv[i, j] = int(h / 2.0)
        s_hsv[i, j] = int(s * 255)
        v_hsv[i, j] = int(v * 255)


# SHOW IMAGE

cv2.imshow("Asli (RGB/BGR)", img)

# Display RGB Channel
cv2.imshow("1. RGB - Red Channel", img_r)
cv2.imshow("1. RGB - Green Channel", img_g)
cv2.imshow("1. RGB - Blue Channel", img_b)

# Display CMYK
cv2.imshow("2. CMYK - Cyan", c_img)
cv2.imshow("2. CMYK - Magenta", m_img)
cv2.imshow("2. CMYK - Yellow", y_img)
cv2.imshow("2. CMYK - Key (Black)", k_img)

# Display HSI
cv2.imshow("3. HSI - Hue", h_hsi)
cv2.imshow("3. HSI - Saturation", s_hsi)
cv2.imshow("3. HSI - Intensity", i_hsi)

# Display HSV
cv2.imshow("4. HSV - Hue", h_hsv)
cv2.imshow("4. HSV - Saturation", s_hsv)
cv2.imshow("4. HSV - Value", v_hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()