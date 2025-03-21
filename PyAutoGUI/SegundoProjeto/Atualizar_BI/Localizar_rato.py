import pyautogui
import time

# Função para obter coordenadas do mouse
def get_mouse_position():
    x, y = pyautogui.position()
    return x, y

# Script principal
if __name__ == "__main__":
    print("Posicione o mouse no ponto desejado e aguarde 10 segundos...")
    time.sleep(5)  # Espera 5 segundos para o usuário posicionar o mouse
    x, y = get_mouse_position()
    print(f"Coordenadas obtidas: X={x}, Y={y}")
