import cv2

cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open video.")
#     exit()

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

    # cv2.imshow('Video Frame', frame)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Gray Frame', gray)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     break


# fps = cap.get(cv2.CAP_PROP_FPS)
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# print(f"Vidéo : FPS:{fps}, Width: {width}, Height: {height}")

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 30.0, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

out.release()
cv2.destroyAllWindows()




