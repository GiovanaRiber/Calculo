import cv2
import numpy as np

def rgb_para_hsi(image):
    # normalizar os valores de R, G e B
    image = image.astype(np.float32) / 255
    R, G, B = cv2.split(image)
    
    # cálculo do componente de intensidade
    I = (R + G + B) / 3
    
    # cálculo do componente de saturação
    min_val = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-6)) * min_val
    S[I == 0] = 0
    
    # cálculo do componente de matiz
    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + 1e-6
    theta = np.arccos(num / den)
    H = np.where(B > G, 2 * np.pi - theta, theta)
    H = H / (2 * np.pi)  
    
    return cv2.merge((H, S, I))

def hsi_para_rgb(hsi_image):
    H, S, I = cv2.split(hsi_image)
    H = H * (2 * np.pi)  # converter para radianos
    
    R, G, B = np.zeros_like(H), np.zeros_like(H), np.zeros_like(H)
    
    # região 0 <= H < 2pi/3
    idx = (H < 2 * np.pi / 3)
    B[idx] = I[idx] * (1 - S[idx])
    R[idx] = I[idx] * (1 + (S[idx] * np.cos(H[idx])) / np.cos(np.pi / 3 - H[idx]))
    G[idx] = 3 * I[idx] - (R[idx] + B[idx])
    
    # região 2pi/3 <= H < 4pi/3
    idx = (H >= 2 * np.pi / 3) & (H < 4 * np.pi / 3)
    H[idx] -= 2 * np.pi / 3
    R[idx] = I[idx] * (1 - S[idx])
    G[idx] = I[idx] * (1 + (S[idx] * np.cos(H[idx])) / np.cos(np.pi / 3 - H[idx]))
    B[idx] = 3 * I[idx] - (R[idx] + G[idx])
    
    # região 4pi/3 <= H < 2pi
    idx = (H >= 4 * np.pi / 3)
    H[idx] -= 4 * np.pi / 3
    G[idx] = I[idx] * (1 - S[idx])
    B[idx] = I[idx] * (1 + (S[idx] * np.cos(H[idx])) / np.cos(np.pi / 3 - H[idx]))
    R[idx] = 3 * I[idx] - (G[idx] + B[idx])
    
    # converter para [0,255] e combinar canais
    rgb_image = np.clip(cv2.merge((R, G, B)) * 255, 0, 255).astype(np.uint8)
    return rgb_image

image = cv2.imread('imagem_redimensionada.jpg')
hsi_image = rgb_para_hsi(image)
rgb_convertida = hsi_para_rgb(hsi_image)

cv2.imwrite('imagem_hsi.jpg', (hsi_image * 255).astype(np.uint8))
cv2.imwrite('imagem_rgb_convertida.jpg', rgb_convertida)