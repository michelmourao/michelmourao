import cv2
import numpy as np
from random import randint
import os
import sys

currently_path = os.getcwd()

project_path = "michelmourao/Computer vision/Tracker" #If Macos use '/' and if Windows use '\'
folder_path = os.path.join(currently_path, project_path)
#print(folder_path)
archive = "futebol.mp4"
full_path = os.path.join(folder_path, archive)
#print(full_path)
print("file exists?", os.path.exists(full_path))


cap = cv2.VideoCapture(full_path)

ok, frame = cap.read()
if not ok:
    print(f'It was not possible to read {archive}')
    sys.exit(1)

bboxes = []
colors = []

while True:
    bbox = cv2.selectROI('Tracker', frame)
    bboxes.append(bbox)
    colors.append((randint(0, 254), randint(0, 254), randint(0, 254)))
    print('Press "Q" to quit or any other to next object')
    k = cv2.waitKey(0) & 0XFF
    if k == 113:
        break

print(f'Bboxes: {bboxes}')

tracker = cv2.legacy.TrackerCSRT_create()
multitracker = cv2.legacy.TrackerCSRT_create()

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break

    ok, boxes = multitracker.update(frame)

    for i , newbox in enumerate(boxes):
        (x,y,w,h) = [int(v) for v in newbox]
        cv2.rectangle(frame, (x,y), (x+y, y+h), colors[i], 2,1)

    cv2.imshow('MultiTracker', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break