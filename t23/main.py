# Sebastian Barceinas, Mael Treviño
from captura import capture_screen
from registro import log_processes

def main():
    try:
        capture_screen()
        log_processes()   
    except Exception as e:
        print(f"Error en la ejecución del script: {e}")

if __name__ == "__main__":
    main()
