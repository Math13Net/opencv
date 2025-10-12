import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#     edges_1 = cv2.Canny(frame, 100, 200)
#     edges_2 = cv2.Canny(blurred, 100, 200)
#     cv2.imshow('Edges Detection sans BLUR', edges_1)
#     cv2.imshow('Edges Detection avec BLUR', edges_2)

#     if cv2.waitKey(1)& 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


def nothing(x):
    pass    

cv2.namedWindow('Edges Detection avec BLUR')
cv2.createTrackbar('Min', 'Edges Detection avec BLUR', 100, 255, nothing)
cv2.createTrackbar('Max', 'Edges Detection avec BLUR', 200, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    min_val = cv2.getTrackbarPos('Min', 'Edges Detection avec BLUR')
    max_val = cv2.getTrackbarPos('Max', 'Edges Detection avec BLUR')

    edges = cv2.Canny(blurred, min_val, max_val)
    cv2.imshow('Edges Detection avec BLUR', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()