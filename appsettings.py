import os
from dotenv import load_dotenv

load_dotenv()

class AppSettings:
    # URL de la API de universidades
    UNIVERSITIES_URL = "http://universities.hipolabs.com/search"

    # Tiempo máximo de espera para la petición
    TIMEOUT_SECONDS = 10