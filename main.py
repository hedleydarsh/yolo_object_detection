import cv2
import glob
import os
import matplotlib.pyplot as plt
from ultralytics import YOLO
from PIL import Image

# Criar pasta output se não existir
os.makedirs("output", exist_ok=True)

# Carregar o modelo YOLOv8 pré-treinado no COCO
model = YOLO("yolov8x.pt")

# Pegar todas as imagens na pasta images/
image_paths = glob.glob("images/*.jpeg")

# Criar variável para armazenar a contagem de objetos detectados
detections_count = {}

# Processar cada imagem
for img_path in image_paths:
    img_name = os.path.basename(img_path)
    
    print(f"Processando {img_name}...")  # Para depuração

    # Fazer a detecção
    results = model(img_path)

    # Garantir que os resultados sejam salvos corretamente
    save_path = f"output/{img_name}"
    results[0].save(filename=save_path)
    print(f"Imagem salva em {save_path}")

    # Contar as classes detectadas
    for r in results:
        for c in r.boxes.cls:
            class_name = model.names[int(c)]
            detections_count[class_name] = detections_count.get(class_name, 0) + 1
            
# Exibir cada imagem processada para conferência
for img_path in glob.glob("output/*.jpeg"):
    example_image = Image.open(img_path)
    plt.figure()
    plt.imshow(example_image)
    plt.axis("off")
    plt.title(f"Detecção em {os.path.basename(img_path)}")
    plt.show()

print("Detecções por classe:", detections_count)

# Criar gráfico de barras com as classes detectadas
plt.figure(figsize=(8, 4))
plt.bar(detections_count.keys(), detections_count.values(), color="skyblue")
plt.xlabel("Classes")
plt.ylabel("Quantidade Detectada")
plt.title("Distribuição dos Objetos Detectados")
plt.xticks(rotation=45)
plt.show()

