import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

ret, frame_1 = cap.read()
if not ret:
    print("Error: Could not read frame.")
    exit() 

gray_1 = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
gray_1 = cv2.GaussianBlur(gray_1, (21, 21), 0)

while cap.isOpened():
    ret, frame_2 = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    frame_2 = cv2.flip(frame_2, 1)

    gray_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)
    gray_2 = cv2.GaussianBlur(gray_2, (21, 21), 0)

    diff = cv2.absdiff(gray_1, gray_2)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresh = cv2.dilate(thresh, kernel, iterations=2)

    frame_2[thresh == 255] = [0, 255, 0]

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame_2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Motion Detection", frame_2)
    gray_1 = gray_2
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()










