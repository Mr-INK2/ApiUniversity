"""
=============================================================================
DATA TRANSFER OBJECTS (DTOs) - MODELOS DE RESPUESTA
=============================================================================
Este módulo define las estructuras de datos que la API devuelve al cliente.
Utiliza Pydantic para la validación de tipos y la generación automática de 
esquemas JSON.

El objetivo de este DTO es actuar como un contrato de datos que asegura que
solo se entregue información relevante y estructurada.
=============================================================================
"""

from pydantic import BaseModel, Field
from typing import List

class UniversityResponseDTO(BaseModel):
    """
    Modelo de respuesta para la información básica de una universidad.
    
    Este modelo representa la 'Respuesta Estructurada' final, habiendo
    descartado campos redundantes o innecesarios de la API externa.
    """

    name: str = Field(
        ..., 
        description="Nombre oficial de la institución educativa",
        examples=["Universidad Nacional de Colombia"]
    )

    web_pages: List[str] = Field(
        ...,
        description="Lista de sitios web oficiales de la universidad",
        examples=[["http://www.unal.edu.co/"]]
    )

    class Config:
        """
        Configuración adicional para la documentación de OpenAPI (Swagger).
        """
        json_schema_extra = {
            "example": {
                "name": "Universidad Nacional de Colombia",
                "web_pages": ["http://www.unal.edu.co/"]
            }
        }