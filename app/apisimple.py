# mi_app/api_client.py

import requests

BASE_URL = 'https://apisimple-9acb.onrender.com/'

def get_data(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Puedes definir funciones adicionales para diferentes endpoints si es necesario
