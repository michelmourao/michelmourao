import cv2
import numpy as np
from random import randint
import os

currently_path = os.getcwd()

project_path = "michelmourao\Computer vision\Tracker"
folder_path = os.path.join(currently_path, project_path)
#print(folder_path)
archive = "futebol.mp4"
full_path = os.path.join(folder_path, archive)
#print(full_path)

print("file exists?", os.path.exists(full_path))

cap = cv2.VideoCapture(full_path)

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow('MultiTracker', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break