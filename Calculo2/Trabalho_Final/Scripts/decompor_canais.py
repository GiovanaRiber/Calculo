import cv2
import numpy as np

def decompor_rgb_hsi(imagem_path):
    image = cv2.imread(imagem_path)
    
    B, G, R = cv2.split(image)
    
    # converter para HSI
    hsi_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    H, S, I = cv2.split(hsi_image)
    
    cv2.imwrite('imagem_R.jpg', R)
    cv2.imwrite('imagem_G.jpg', G)
    cv2.imwrite('imagem_B.jpg', B)

    cv2.imwrite('imagem_H.jpg', H)
    cv2.imwrite('imagem_S.jpg', S)
    cv2.imwrite('imagem_I.jpg', I)
    
    print("Imagens decompostas salvas: componentes RGB e HSI")

decompor_rgb_hsi('imagem_redimensionada.jpg')
