import cv2
import numpy as np

def aplicar_filtros_suavizacao(imagem_path):

    image = cv2.imread(imagem_path)
    
    # definir máscaras de suavização
    mask_3x3 = np.ones((3, 3), dtype=np.float32) / 9
    mask_5x5 = np.ones((5, 5), dtype=np.float32) / 25
    mask_7x7 = np.ones((7, 7), dtype=np.float32) / 49
    
    # aplicar os filtros
    result_3x3 = cv2.filter2D(image, -1, mask_3x3)
    result_5x5 = cv2.filter2D(image, -1, mask_5x5)
    result_7x7 = cv2.filter2D(image, -1, mask_7x7)
    
    cv2.imwrite('imagem_suavizada_3x3.jpg', result_3x3)
    cv2.imwrite('imagem_suavizada_5x5.jpg', result_5x5)
    cv2.imwrite('imagem_suavizada_7x7.jpg', result_7x7)
    
    print("Imagens suavizadas salvas: 'imagem_suavizada_3x3.jpg', 'imagem_suavizada_5x5.jpg', 'imagem_suavizada_7x7.jpg'")

aplicar_filtros_suavizacao('imagem_com_ruido.jpg')
