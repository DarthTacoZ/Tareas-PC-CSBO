import subprocess
from datetime import datetime

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
