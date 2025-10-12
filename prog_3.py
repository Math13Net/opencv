import cv2

# webcam : 0 (ou mets un chemin de fichier vidéo)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (320, 240), interpolation=cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 100, 200)
    edge_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    overlay = cv2.addWeighted(frame, 0.8, edge_color, 0.2, 0)

    cv2.imshow('Overlay Frame', overlay)
    cv2.imshow('Frame de départ réduite', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





