import cv2
import numpy as np

def adicionar_ruido(imagem_path, escala=0.1, stddev=25):

    image = cv2.imread(imagem_path)
    
    # reduzindo a escala
    resized_image = cv2.resize(image, (0, 0), fx=escala, fy=escala)
    
    # gerar ruído gaussiano
    ruido = np.random.normal(0, stddev, resized_image.shape).astype(np.uint8)
    noisy_image = cv2.add(resized_image, ruido)
    
    # garantir valores no intervalo [0, 255]
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    
    cv2.imwrite('imagem_redimensionada.jpg', resized_image)
    cv2.imwrite('imagem_com_ruido.jpg', noisy_image)

# exemplo de uso
adicionar_ruido('imagem_original.jpg')
