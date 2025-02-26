import cv2
import numpy as np
import matplotlib.pyplot as plt

def gradiente_sobel_vetorial(imagem):
    # separando os canais RGB
    r, g, b = cv2.split(imagem)

    # gradientes em x e y para cada canal
    dr_dx = cv2.Sobel(r, cv2.CV_64F, 1, 0, ksize=3)
    dr_dy = cv2.Sobel(r, cv2.CV_64F, 0, 1, ksize=3)
    dg_dx = cv2.Sobel(g, cv2.CV_64F, 1, 0, ksize=3)
    dg_dy = cv2.Sobel(g, cv2.CV_64F, 0, 1, ksize=3)
    db_dx = cv2.Sobel(b, cv2.CV_64F, 1, 0, ksize=3)
    db_dy = cv2.Sobel(b, cv2.CV_64F, 0, 1, ksize=3)

    # cálculo dos vetores gradientes
    g_xx = dr_dx**2 + dg_dx**2 + db_dx**2
    g_yy = dr_dy**2 + dg_dy**2 + db_dy**2
    g_xy = dr_dx * dr_dy + dg_dx * dg_dy + db_dx * db_dy

    # ângulo da direção de máxima variação
    theta = 0.5 * np.arctan2(2 * g_xy, g_xx - g_yy)

    # magnitude máxima de variação
    f_theta = np.sqrt(
        0.5 * (g_xx + g_yy)
        + 0.5 * (g_xx - g_yy) * np.cos(2 * theta)
        + 2 * g_xy * np.sin(2 * theta)
    )
    
    # normalizar 
    f_theta_normalizado = cv2.normalize(f_theta, None, 0, 255, cv2.NORM_MINMAX)

    return np.uint8(f_theta_normalizado)

def gradiente_sobel_tradicional(imagem):

    r, g, b = cv2.split(imagem)

    # aplicando o gradiente de Sobel em cada canal
    sobel_rx = cv2.Sobel(r, cv2.CV_64F, 1, 0, ksize=3)
    sobel_ry = cv2.Sobel(r, cv2.CV_64F, 0, 1, ksize=3)
    sobel_gx = cv2.Sobel(g, cv2.CV_64F, 1, 0, ksize=3)
    sobel_gy = cv2.Sobel(g, cv2.CV_64F, 0, 1, ksize=3)
    sobel_bx = cv2.Sobel(b, cv2.CV_64F, 1, 0, ksize=3)
    sobel_by = cv2.Sobel(b, cv2.CV_64F, 0, 1, ksize=3)

    # calculando a magnitude do gradiente para cada canal
    magnitude_r = np.sqrt(sobel_rx**2 + sobel_ry**2)
    magnitude_g = np.sqrt(sobel_gx**2 + sobel_gy**2)
    magnitude_b = np.sqrt(sobel_bx**2 + sobel_by**2)

    # combinando as magnitudes dos três canais (em escala de cinza)
    magnitude_combined = np.sqrt(magnitude_r**2 + magnitude_g**2 + magnitude_b**2)

    # normalizando a magnitude para o intervalo de 0 a 255
    magnitude_combined = np.uint8(cv2.normalize(magnitude_combined, None, 0, 255, cv2.NORM_MINMAX))

    return magnitude_combined

def salvar_plot(imagem, nome_arquivo):
    plt.figure(figsize=(6, 6))
    plt.imshow(imagem, cmap="gray")
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(nome_arquivo, bbox_inches='tight', pad_inches=0)

def processar_gradiente(imagem_path):
    imagem = cv2.imread(imagem_path)

    resultado_vetorial = gradiente_sobel_vetorial(imagem)
    resultado_tradicional = gradiente_sobel_tradicional(imagem)

    salvar_plot(resultado_vetorial, 'resultado_vetorial_plot.jpg')
    salvar_plot(resultado_tradicional, 'resultado_tradicional_plot.jpg')

processar_gradiente('modelo_suavizada.jpg')
