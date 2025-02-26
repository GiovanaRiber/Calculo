import cv2
import numpy as np

def aplicar_operadores_gradiente(imagem_path):
   
    image = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    
    # operador de Roberts
    kernel_roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
    kernel_roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
    roberts_x = cv2.filter2D(image, -1, kernel_roberts_x)
    roberts_y = cv2.filter2D(image, -1, kernel_roberts_y)
    roberts = cv2.addWeighted(roberts_x, 0.5, roberts_y, 0.5, 0)
    
    # operador de Prewitt
    prewitt_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    prewitt_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    prewitt = cv2.addWeighted(prewitt_x, 0.5, prewitt_y, 0.5, 0)
    
    # operador de Sobel
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    
    roberts = np.uint8(np.absolute(roberts))
    prewitt = np.uint8(np.absolute(prewitt))
    sobel = np.uint8(np.absolute(sobel))
    
    cv2.imwrite('gradient_roberts.jpg', roberts)
    cv2.imwrite('gradient_prewitt.jpg', prewitt)
    cv2.imwrite('gradient_sobel.jpg', sobel)
    
aplicar_operadores_gradiente('imagem_redimensionada.jpg')