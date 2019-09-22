import os
y = os.listdir(os.getcwd())

for i in range(len(y)):
	if 'mp4' in y[i]:
		path = y[i]

import cv2 
cap = cv2.VideoCapture(path)
Cascade = cv2.CascadeClassifier("haarCasade.xml")
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break
    cap.release()
    cv2.destroyAllWindows()