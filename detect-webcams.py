import cv2

for i in range(5):  # Testa os primeiros 5 índices
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Webcam encontrada no índice {i}")
        cap.release()
