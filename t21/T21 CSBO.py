import requests
import json
import logging
import getpass

# Solicitar la API Key de manera segura
key = getpass.getpass("Por favor, ingrese su API Key de Have I Been Pwned: ")

# Configurar encabezados para la solicitud
headers = {
    'content-type': 'application/json',
    'hibp-api-version': '3',
    'User-Agent': 'python',
    'Authorization': f'Bearer {key}'  # Autenticación usando Bearer Token
}

# Solicitar el correo a investigar
email = input("Ingrese el correo a investigar: ")
url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false'

# Configuración del log
logging.basicConfig(filename='hibpINFO.log', 
                    format='%(asctime)s %(message)s', 
                    datefmt='%m/%d/%Y %I:%M:%S %p', 
                    level=logging.INFO)

try:
    # Realizar la solicitud a la API
    r = requests.get(url, headers=headers)
    r.raise_for_status()  # Verifica si hubo errores HTTP

    data = r.json()

    # Verificar si hubo filtraciones
    if r.status_code == 200 and data:
        encontrados = len(data)
        print(f"¡Los datos que se han filtrado del correo {email} son:")
        for filtracion in data:
            print(f"Nombre: {filtracion['Name']}")
            print(f"Dominio: {filtracion.get('Domain', 'No disponible')}")
            print(f"Fecha de la filtración: {filtracion.get('BreachDate', 'No disponible')}")
            print(f"Descripción: {filtracion.get('Description', 'No disponible')}")
            print("\n")
        msg = f"{email} - Filtraciones encontradas: {str(encontrados)}"

        # Guardar un reporte en un archivo de texto
        with open('reporte_filtraciones.txt', 'w') as f:
            f.write(f"Reporte de filtraciones para {email}:\n\n")
            for filtracion in data:
                f.write(f"Nombre: {filtracion['Name']}\n")
                f.write(f"Dominio: {filtracion.get('Domain', 'No disponible')}\n")
                f.write(f"Fecha de la filtración: {filtracion.get('BreachDate', 'No disponible')}\n")
                f.write(f"Descripción: {filtracion.get('Description', 'No disponible')}\n")
                f.write("\n")

    else:
        print(f"El correo {email} no ha sido filtrado.")
        msg = f"{email} no tiene filtraciones"

except requests.exceptions.RequestException as e:
    # Manejo de cualquier error de la API o de la red
    logging.error(f"Error al realizar la solicitud: {e}")
    msg = f"Error al verificar el correo {email}: {e}"

finally:
    # Registrar el resultado en el log
    logging.info(msg)
    print("El resultado ha sido registrado en el archivo de log.")
