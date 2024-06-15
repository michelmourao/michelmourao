import cv2
import numpy as np
from random import randint

vaga1 = [1, 89, 108, 213]
vaga2 = [115, 87, 152, 211]
vaga3 = [289, 89, 138, 212]
vaga4 = [439, 87, 135, 212]
vaga5 = [591, 90, 132, 206]
vaga6 = [738, 93, 139, 204]
vaga7 = [881, 93, 138, 201]
vaga8 = [1027, 94, 147, 202]

vagas = [vaga1, vaga2, vaga3, vaga4, vaga5, vaga6, vaga7, vaga8]

video = cv2.VideoCapture('video.mp4')

if not video.isOpened():
    print('Load Error')

else:
    while True:
        check, img = video.read()
        if not check:
            print('Read Error')
            break

        cv2.imshow('video', img)
        cv2.waitKey(10)