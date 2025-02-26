import cv2
import numpy as np

def calcular_diferenca(imagem1_path, imagem2_path, output_path):
 
    imagem1 = cv2.imread(imagem1_path)
    imagem2 = cv2.imread(imagem2_path)
    
    # garantir que ambas as imagens tenham o mesmo tamanho
    if imagem1.shape != imagem2.shape:
        raise ValueError("As imagens devem ter o mesmo tamanho para calcular a diferença.")
    
    # calcular a diferença absoluta entre as imagens
    diferenca = np.abs(imagem1.astype(np.float32) - imagem2.astype(np.float32))
    
    # normalizar os valores 
    diferenca = (diferenca / np.max(diferenca)) * 255
    diferenca = diferenca.astype(np.uint8)
    
    # converter para escala de cinza
    diferenca_gray = cv2.cvtColor(diferenca, cv2.COLOR_BGR2GRAY)
    
    cv2.imwrite(output_path, diferenca_gray)
    
calcular_diferenca('imagem_rgb_suavizada.jpg', 'imagem_hsi_suavizada.jpg', 'imagem_diferenca.jpg')