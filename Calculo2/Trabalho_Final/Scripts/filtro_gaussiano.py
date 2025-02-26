import cv2

def aplicar_filtro_gaussiano(imagem_path, sigma1=3, sigma2=13):

    image = cv2.imread(imagem_path)
    
    # aplicar o filtro Gaussiano com diferentes desvios padrão
    gaussian_blurred_low = cv2.GaussianBlur(image, (11, 11), sigma1)
    gaussian_blurred_high = cv2.GaussianBlur(image, (11, 11), sigma2)
    
    cv2.imwrite('imagem_gaussiana_desvio_baixo.jpg', gaussian_blurred_low)
    cv2.imwrite('imagem_gaussiana_desvio_alto.jpg', gaussian_blurred_high)

aplicar_filtro_gaussiano('imagem_redimensionada.jpg')
