"""
=============================================================================
PUNTO DE ENTRADA DE LA API DE UNIVERSIDADES
=============================================================================
Este archivo inicializa la aplicación FastAPI y registra los controladores
necesarios para el consumo de la API externa de Hipolabs[cite: 18, 28].

Para ejecutar localmente:
    uvicorn main:app --reload

Documentación automática:
    - Swagger UI: http://localhost:8000/docs
=============================================================================
"""

from fastapi import FastAPI
# Importamos tu router específico de universidades
from controllers.universitycontroller import router as university_router

# =============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN
# =============================================================================
app = FastAPI(
    title="University Finder API",
    description="""
    ## API de Consulta Universitaria 
    
    Esta API permite obtener un listado de instituciones de educación superior 
    por país, procesando datos de la API pública de Hipolabs[cite: 35, 43].
    
    """,
    version="1.0.0",
    contact={
        "name": "Tu Nombre",
        "email": "tu@email.com"
    }
)

# =============================================================================
# ENDPOINT RAÍZ
# =============================================================================
@app.get("/", tags=["General"])
def home():
    """
    Mensaje de bienvenida y estado de la API.
    """
    return {
        "message": "Bienvenido a la University API",
        "docs": "Visita /docs para la documentación interactiva",
        "status": "Ready"
    }

# =============================================================================
# REGISTRO DE RUTERS [cite: 29]
# =============================================================================
# Registramos las rutas del controlador de universidades
app.include_router(university_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)