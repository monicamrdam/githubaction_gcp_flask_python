import os
from dotenv import load_dotenv

# Carga las variables de entorno en memoria
load_dotenv()  # Cargar todo el contenido de .env en variables de entorno


class Config:
    URL_PORT = os.environ.get('secrets.URL_PORT')

    URL_Search = 'https://api.spotify.com/v1/search'
    URL_Artist = 'https://api.spotify.com/v1/artists'

    CLIENT_ID = os.environ.get('secrets.CLIENT_ID', "")  # O devuelve la variable de entorno o la cadena vacia
    CLIENT_SECRET = os.environ.get('secrets.CLIENT_SECRET', "")  # O devuelve la variable de entorno o la cadena vacia


