import pyautogui
import subprocess
from datetime import datetime

# Función para capturar la pantalla
def capture_screen():
    # Obtener la fecha y hora actual para el nombre del archivo
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'screenshot_{timestamp}.png'
    # Tomar la captura
    screenshot = pyautogui.screenshot()
    # Guardar la captura
    screenshot.save(filename)
    print(f"Captura de pantalla guardada como {filename}")

# Función para registrar los procesos en ejecución
def log_processes():
    try:
        # Obtener la fecha y hora actual para el nombre del archivo
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'process_log_{timestamp}.txt'
        # Procesos en ejecución
        result = subprocess.run(['tasklist'], capture_output=True, text=True, shell=True)
        # Guardar en un archivo de texto
        with open(filename, 'w') as file:
            file.write(result.stdout)
        print(f"Registro de procesos guardado como {filename}")
    except Exception as e:
        print(f"Error al registrar los procesos: {e}")

# Función principal que ejecuta ambas acciones
def main():
    try:
        capture_screen()
        log_processes()   
    except Exception as e:
        print(f"Error en la ejecución del script: {e}")

if __name__ == "__main__":
    main()
