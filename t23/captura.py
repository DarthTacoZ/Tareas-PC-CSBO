import pyautogui
from datetime import datetime

def capture_screen():
    # Obtener la fecha y hora actual para el nombre del archivo
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'screenshot_{timestamp}.png'
    # Tomar la captura
    screenshot = pyautogui.screenshot()
    # Guardar la captura
    screenshot.save(filename)
    print(f"Captura de pantalla guardada como {filename}")
