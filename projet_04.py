import cv2
import time

#Initialize video capture
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Set initial resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Frame rate counter
start_time = time.time()
frame_count = 0
while cap.isOpened():
    ret, frame_ = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Basic processing
    gray = cv2.cvtColor(frame_, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    # Display frame rate
    frame_count += 1
    elapsed = time.time() - start_time
    if elapsed > 1:
        fps = frame_count / elapsed
        cv2.putText(frame_, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        frame_count = 0
        start_time = time.time()

    cv2.imshow('Optimized processing', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
