# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:20:44 2026

@author: Sarah SM
"""

import cv2

# 1. READ IMAGE

img = cv2.imread("images/kontras.jpeg")


# 2. SHOW IMAGE

cv2.imshow("Foto Kontras", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 3. FILTER COLOR IMAGE

img = cv2.imread("images/kontras.jpeg")

(w, h, c) = img.shape

for i in range(w):
    for j in range(h):
        img[i, j, 0] = 0
        img[i, j, 2] = 0

cv2.imshow("Filter Hijau", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# 4. FILTER COLOR VIDEO

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    if not ret:
        print("Tidak bisa membaca webcam")
        break

    (w, h, c) = frame.shape

    for i in range(w):
        for j in range(h):
            frame[i, j, 0] = 0
            frame[i, j, 2] = 0

    cv2.imshow("Filter Hijau", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()