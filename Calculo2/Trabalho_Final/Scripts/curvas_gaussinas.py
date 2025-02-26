import numpy as np
import matplotlib.pyplot as plt

def plot_gaussian_curves():
    # valores para x
    x = np.linspace(-10, 10, 500)

    # parâmetros da curva Gaussiana
    mu = 0  # média
    std_devs = [1, 2, 3]  # diferentes valores de desvio padrão
    colors = ['#800080', '#40E0D0', '#FF6347']  # cores

    plt.figure(figsize=(10, 6))

    for sigma, color in zip(std_devs, colors):
        gaussian = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
        plt.plot(x, gaussian, label=f"\u03c3 = {sigma}", color=color, linewidth=2)

    plt.title("Curvas Gaussianas", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("G(x)", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

plot_gaussian_curves()
