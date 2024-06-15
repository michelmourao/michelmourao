import cv2
import numpy as np
from random import randint
import os
print("file exists?", os.path.exists('futebol.mp4'))

cap = cv2.VideoCapture("futebol.mp4")

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow('MultiTracker', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break