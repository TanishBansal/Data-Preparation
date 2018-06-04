
import cv2
import math

videoFile = "test10.mp4"
imagesFolder = "images"
cap = cv2.VideoCapture(videoFile)
frame_num = 0
image_num = 10596
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        if frame_num % (30 // 3) == 0:
            cv2.imwrite("D:\Giscle Internship\data"+"/image{}.jpg".format(image_num),frame)
            image_num += 1
    else:
        break
    frame_num += 1
cap.release()
print ("Done!")