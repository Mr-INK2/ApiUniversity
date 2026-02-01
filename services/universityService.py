"""
=============================================================================
CAPA DE SERVICIOS (LOGICA DE NEGOCIO)
=============================================================================
Este módulo se encarga de procesar la lógica de la aplicación, actuando como
intermediario entre el Cliente (API externa) y el Controlador.

Responsabilidades:
- Limpieza y validación de parámetros de entrada.
- Transformación de datos crudos (JSON) a objetos estructurados (DTOs).
- Filtrado de información no deseada.
=============================================================================
"""

import httpx
from clients.universityClient import UniversityClient
from DTOs.universityDtos import UniversityResponseDTO

class UniversityService:
    """
    Servicio especializado en la gestión de información universitaria.
    """

    def __init__(self):
        # Inicializamos el cliente que conecta con Hipolabs
        self.client = UniversityClient()

    async def get_universities(self, country: str, http_client: httpx.AsyncClient) -> list[UniversityResponseDTO]:
        """
        Obtiene y filtra el listado de universidades de un país específico.

        Este método implementa la "Respuesta Estructurada" exigida en el taller,
        eliminando datos redundantes como el código del país o dominios adicionales.

        Args:
            country (str): Nombre del país a consultar.
            http_client (httpx.AsyncClient): Cliente para realizar la petición asíncrona.

        Returns:
            list[UniversityResponseDTO]: Lista de objetos limpios con nombre y web. [cite: 39, 53]
        """
        # Limpieza de espacios en el parámetro de entrada
        country = country.strip()
        
        # Consumimos la API externa usando el cliente adaptado [cite: 33, 35]
        raw_data = await self.client.get_universities_by_country(country, http_client)

        # Mapeo selectivo: Se transforma la "basura cruda" en una respuesta estructurada 
        # Se decidió omitir el campo 'country' en la respuesta por ser redundante [cite: 54, 59]
        return [
            UniversityResponseDTO(
                name=uni["name"],
                web_pages=uni.get("web_pages", [])
            )
            for uni in raw_data
        ]