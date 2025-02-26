import cv2
import numpy as np

def suavizar_rgb_hsi(imagem_path):

    image = cv2.imread(imagem_path)
    
    # separar canais RGB
    B, G, R = cv2.split(image)
    
    # aplicar suavização em cada canal RGB
    kernel = np.ones((5, 5), np.float32) / 25
    R_suavizado = cv2.filter2D(R, -1, kernel)
    G_suavizado = cv2.filter2D(G, -1, kernel)
    B_suavizado = cv2.filter2D(B, -1, kernel)
    
    # recombinar canais RGB
    imagem_rgb_suavizada = cv2.merge((B_suavizado, G_suavizado, R_suavizado))
    
    # converter para HSI
    hsi_image = rgb_para_hsi(image)
    H, S, I = cv2.split(hsi_image)
    
    # suavizar apenas o canal de intensidade
    I_suavizado = cv2.filter2D(I, -1, kernel)
    hsi_suavizado = cv2.merge((H, S, I_suavizado))
    imagem_hsi_suavizada = hsi_para_rgb(hsi_suavizado)
    
    cv2.imwrite('imagem_rgb_suavizada.jpg', imagem_rgb_suavizada)
    cv2.imwrite('imagem_hsi_suavizada.jpg', imagem_hsi_suavizada)

suavizar_rgb_hsi('imagem_redimensionada.jpg')
