import numpy as np
import cv2
import sys
imagePath = sys.argv[1]
cascPath = sys.argv[2]
faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtcolor(image,cv2,COLOR_BGR2FRAY)

faces = faceCascade.detectMultiscale(
    gray,
    scalefactor = 1.1,
    minneighbours = 5,
    minsize = (30,30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!").format(len(faces))

for(x,y,w,h) in faces:
    cv2.rec(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("faces found",image)
cv2.waitKey(0)