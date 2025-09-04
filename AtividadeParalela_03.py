# Open CV
# Instalado via pip install opencv-python, pip install matplotlib e pip install numpy
import os
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("results", exist_ok=True)

img_path = "carro.jpg"

img = cv.imread(img_path, cv.IMREAD_COLOR)

# Redimensiona a imagem, para ter metade do seu tamanho original
img_half = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

# Redimensiona a imagem para ser maior
img_double = cv.resize(img, (img.shape[1] * 2, img.shape[0] * 2))

# Salva as imagens dos resultados
cv.imwrite("results/car_half.jpg", img_half)
cv.imwrite("results/car_double.jpg", img_double)

img_h_flip = img[:, ::-1]

# Precisa converter de BGR para RGB, pois o matplotlib usa RGB, diferente do
# OpenCV que usa BGR
img_h_flip_rgb = cv.cvtColor(img_h_flip, cv.COLOR_BGR2RGB)

plt.imshow(img_h_flip_rgb)
plt.title("Imagem com flip horizontal")
plt.show()

# Agora, vou recortar uma região no centro da imagem
# Primeiro, eu vou definir as coordenadas iniciais, X e Y, começando por x1 até x2 e y1 até y2
# Y é de cima para baixo, vertical, sendo 0 até altura-1
# Já no X, é da esquerda para a direita, sendo 0 até largura-1
x1 = 100
y1 = 100
x2 = 400
y2 = 400

img_crop = cv.cvtColor(img[y1:y2, x1:x2], cv.COLOR_BGR2RGB)

plt.imshow(img_crop)
plt.title("Imagem recortada")
plt.show()

img_colored = cv.cvtColor(img, cv.COLOR_BGR2RGB)

zeros = np.zeros(img.shape[:2], dtype="uint8")

#Aqui separa os canais de cor
b, g, r = cv.split(img_colored)

#Imagem com verde + vermelho
img_gr = cv.merge([zeros, g, r])

#Imagem com azul + vermelho
img_br = cv.merge([b, zeros, r])

#Imagem com azul + verde
img_bg = cv.merge([b, g, zeros])

plt.imshow(img_gr)
plt.title("Imagem com canais G e R")
plt.show()

plt.imshow(img_br)
plt.title("Imagem com canais B e R")
plt.show()

plt.imshow(img_bg)
plt.title("Imagem com canais B e G")
plt.show()