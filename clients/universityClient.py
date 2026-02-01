"""
=============================================================================
CAPA DE CLIENTES (CONEXIÓN EXTERNA)
=============================================================================
Este módulo se encarga exclusivamente de la comunicación con servicios externos.
Su responsabilidad es realizar las peticiones HTTP, manejar los códigos de 
estado de la red y devolver la información cruda (JSON) a la capa de servicio.

Se utiliza 'httpx' para garantizar que las peticiones sean asíncronas y no
bloqueen el servidor FastAPI.
=============================================================================
"""

import httpx
from fastapi import HTTPException
from appsettings import AppSettings

class UniversityClient:
    """
    Cliente encargado de consumir la API pública de Hipolabs.
    """

    def __init__(self):
        
        pass

    async def get_universities_by_country(self, country: str, http_client: httpx.AsyncClient) -> list:
        """
        Realiza la petición GET a la API externa filtrando por país.

        Args:
            country (str): Nombre del país solicitado por el usuario.
            http_client (httpx.AsyncClient): Cliente HTTP compartido.

        Returns:
            list: Datos crudos obtenidos de la API externa.

        Raises:
            HTTPException: Si la API externa falla (Error 500/400) o si no
                          se encuentran resultados para ese país (Error 404).
        """
        # Petición a la URL configurada en appsettings
        response = await http_client.get(
            AppSettings.UNIVERSITIES_URL,
            params={
                "country": country
            }
        )

        # Validación de respuesta exitosa del servidor externo
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="Error al obtener datos desde la API de Universidades"
            )

        data = response.json()

        # Validación de contenido: Si la lista viene vacía, lanzamos un 404
        # Esto cumple con el requisito de manejo de errores del taller.
        if not data:
            raise HTTPException(
                status_code=404,
                detail=f"No se encontraron universidades en '{country}'."
            )

        return data