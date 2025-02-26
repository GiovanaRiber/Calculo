import cv2
import numpy as np

def aplicar_filtro_laplaciano(imagem_path):
    # carregar a imagem em escala de cinza
    image = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    
    # aplicar o filtro Laplaciano
    laplacian = cv2.Laplacian(image, cv2.CV_64F)
    laplacian = np.uint8(np.absolute(laplacian))

    cv2.imwrite('imagem_laplaciano.jpg', laplacian)
    
aplicar_filtro_laplaciano('imagem_redimensionada.jpg')