import requests
import json
import logging
import getpass
import argparse
import six
import sys

#Integrantes del equipo: Mael Treviño, Sebastian Barceinas


# Versión de Python
if not six.PY3:
    raise Exception("Este script solo puede ejecutarse en Python 3.")
    sys.exit(1)

# Logging
logging.basicConfig(filename='hibpINFO.log',
                    format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %I:%M:%S %p",
                    level=logging.INFO)

# Llave API
api_key = getpass.getpass(prompt="Ingrese su API Key de Have I Been Pwned: ")

# Parametros
parser = argparse.ArgumentParser(description="Verifica si un correo ha sido filtrado en alguna brecha de datos.")
parser.add_argument('email', type=str, help="Correo electrónico a investigar")
args = parser.parse_args()

# Configurar headers con la API key
headers = {
    'content-type': 'application/json',
    'api-version': '3',
    'User-Agent': 'python',
    'hibp-api-key': api_key
}

# URL de la API
url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{args.email}?truncateResponse=false'

# Manejo de excepciones
try:
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        encontrados = len(data)

        if encontrados > 0:
            print(f"Los sitios en los que se ha filtrado el correo {args.email} son:")
            # Reporte
            with open('reporte_filtraciones.txt', 'w') as f:
                for filtracion in data:
                    print(filtracion["Name"])
                    f.write(f'{filtracion["Name"]}\n')
            print(f"Reporte guardado en 'reporte_filtraciones.txt'")
        else:
            print(f"El correo {args.email} no ha sido filtrado.")
        
        msg = f"{args.email} Filtraciones encontradas: {encontrados}"
        logging.info(msg)

    else:
        print(f"Error en la solicitud: {r.status_code} - {r.text}")
        logging.error(f"Error en la solicitud: {r.status_code} - {r.text}")

except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")
    logging.error(f"Error de conexión: {e}")
