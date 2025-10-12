import cv2
import threading
import queue

frame_queue = queue.Queue()
stop_event = threading.Event()  # MODIF: petit drapeau pour demander l'arrêt proprement

def capture_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video.")
        # MODIF: si la capture échoue, on débloque le consommateur
        frame_queue.put(None)
        return

    while not stop_event.is_set():  # MODIF: on s'arrête quand 'q' est pressé côté traitement
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        frame_queue.put(frame)

    cap.release()
    frame_queue.put(None)  # MODIF: sentinelle pour signaler au thread de traitement de sortir

def process_frames():
    while True:
        frame = frame_queue.get()
        if frame is None:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Gray Frame', gray_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            stop_event.set()  # MODIF: on demande à la capture de s'arrêter
            break

    cv2.destroyAllWindows()

capture_thread = threading.Thread(target=capture_frames)
process_thread = threading.Thread(target=process_frames)
capture_thread.start()
process_thread.start()
capture_thread.join()
frame_queue.put(None)
process_thread.join()


