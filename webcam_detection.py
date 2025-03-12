import cv2
import time
import os
from ultralytics import YOLO

# Criar pasta para salvar capturas, se não existir
os.makedirs("captures", exist_ok=True)

# Carregar o modelo YOLOv8 pré-treinado no COCO
model = YOLO("yolo11x.pt")

# Iniciar captura da webcam (0 para webcam padrão)
cap = cv2.VideoCapture(2)

# Ajustar resolução da webcam (opcional)
cap.set(3, 1280)  # Largura
cap.set(4, 720)   # Altura

if not cap.isOpened():
    print("Erro ao acessar a webcam!")
    exit()

frame_count = 0
fps_start_time = time.time()

# Criar janela apenas uma vez
cv2.namedWindow("Detecção ao Vivo - YOLOv8", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Rodar YOLO na imagem da webcam
    results = model(frame)

    # Obter a imagem com detecções
    annotated_frame = results[0].plot()  # Retorna a imagem com bounding boxes desenhados

    # Calcular FPS
    frame_count += 1
    fps_end_time = time.time()
    elapsed_time = fps_end_time - fps_start_time
    fps = frame_count / elapsed_time if elapsed_time > 0 else 0

    # Exibir FPS na tela
    cv2.putText(annotated_frame, f"FPS: {fps:.2f}", (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Mostrar o resultado em uma única janela
    cv2.imshow("Detecção ao Vivo - YOLOv8", annotated_frame)

    # Capturar imagem ao pressionar 's'
    key = cv2.waitKey(10) & 0xFF  # Pequeno delay para evitar excesso de frames
    if key == ord('s'):
        capture_path = f"captures/capture_{time.strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(capture_path, annotated_frame)
        print(f"Imagem salva em {capture_path}")

    # Sair ao pressionar 'q'
    if key == ord('q'):
        break

# Liberar a webcam e fechar janelas
cap.release()
cv2.destroyAllWindows()
