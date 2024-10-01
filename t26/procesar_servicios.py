import subprocess
import openpyxl

# Nombres de los integrantes
#Luis Mael Treviño Mares
#Diego Fernando Betancourt Soto
#Carlos Sebastian Barceinas Olascoaga

# Ejecutar el script de PowerShell y capturar la salida
try:
    result = subprocess.run(['powershell', '-File', 'monitor_servicios.ps1'], capture_output=True, text=True)
    
    # Validar que no haya errores
    if result.returncode != 0:
        print("Error al ejecutar el script de PowerShell:")
        print(result.stderr)
    else:
        output_lines = result.stdout.splitlines()
        headers = output_lines[0].split()  
        data = [line.split(None, 3) for line in output_lines[1:]]

        # Crear libro de Excel
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Servicios"

        sheet.append(headers)

        # Datos de los servicios
        for row in data:
            sheet.append(row)

        # Guardar el archivo
        workbook.save('servicios.xlsx')
        print("Datos exportados a servicios.xlsx correctamente.")

except Exception as e:
    print(f"Se ha producido un error: {e}")
