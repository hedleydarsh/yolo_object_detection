# 📌 Projeto: Detecção de Objetos com YOLOv8

Este projeto implementa um **detector de objetos** utilizando o modelo **YOLOv8** para identificar objetos em imagens e na webcam. O modelo foi treinado no **COCO Dataset**, que reconhece 80 classes de objetos comuns.

---

## 🎯 **Objetivo do Projeto**

✅ **Detectar objetos em imagens** e salvar os resultados automaticamente.  
✅ **Realizar detecção em tempo real via webcam** com exibição ao vivo.  
✅ **Gerar estatísticas dos objetos detectados** e exibir um gráfico de distribuição.

---

## 📂 **Estrutura do Projeto**

```
yolo_object_detection/
│── images/                # Pasta com as imagens a serem analisadas
│── output/                # Pasta onde as imagens detectadas serão salvas
│── captures/              # Pasta onde serão salvas capturas da webcam
│── main.py                # Processa imagens e salva resultados
│── webcam_detection.py     # Detecção de objetos via webcam
│── detect-webcams.py       # Lista webcams disponíveis no sistema
│── requirements.txt       # Dependências do projeto
│── README.md              # Documentação do projeto
```

---

## 🚀 **Como Configurar e Executar o Projeto**

### **1️⃣ Instalar as Dependências**

Antes de rodar o projeto, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

### **2️⃣ Testar quais Webcams estão Disponíveis**

Antes de rodar a detecção ao vivo, descubra qual índice sua webcam utiliza:

```bash
python detect-webcams.py
```

A saída indicará quais webcams estão acessíveis e seus respectivos índices.

---

## 🎥 **Execução do Detector de Objetos**

### **🖼️ Para Processar Imagens**

Coloque imagens na pasta `images/` e execute:

```bash
python main.py
```

Os resultados serão salvos na pasta `output/`, e um **gráfico de distribuição dos objetos detectados** será exibido.

### **🎥 Para Usar a Webcam**

Para rodar a detecção ao vivo, execute:

```bash
python webcam_detection.py
```

Caso tenha mais de uma webcam, edite o arquivo e altere:

```python
cap = cv2.VideoCapture(1)  # Troque "1" pelo índice correto
```

Pressione:

- **'s'** para salvar uma captura com a detecção.
- **'q'** para sair.

---

## 📊 **Exemplo de Saída do Gráfico**

Ao processar imagens, um **gráfico de distribuição dos objetos detectados** é gerado automaticamente.

Se precisar de ajustes, edite `main.py` para alterar a visualização dos resultados.

---

## 🏆 **Conclusão**

Este projeto demonstra como o **YOLOv8** pode ser utilizado para detecção de objetos em imagens e vídeos em tempo real, oferecendo uma implementação simples e eficiente para aplicações de **computer vision**.

---

Caso tenha dúvidas ou sugestões, entre em contato! 🚀
