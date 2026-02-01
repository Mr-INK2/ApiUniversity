# 🎓 Sistema de Consulta de Instituciones Educativas (University API)

Este proyecto implementa una solución de backend utilizando **FastAPI** para la gestión y consulta de datos universitarios globales. El sistema ha sido diseñado bajo estándares de **Clean Architecture**, priorizando la separación de responsabilidades y la eficiencia asíncrona.

## 📋 Especificaciones del Taller

El objetivo principal es la integración con servicios externos y la exposición de una interfaz limpia y optimizada.

### 🌐 Origen de la Información (Data Sourcing)
La API consume datos en tiempo real de la plataforma **Hipolabs University Domains and Names API**, un servicio global que proporciona registros actualizados de instituciones de educación superior.
* **Proveedor**: [Hipolabs](http://universities.hipolabs.com/)
* **Endpoint base**: `http://universities.hipolabs.com/search`

### ⚡ Optimización y Limpieza de Respuesta
Uno de los pilares de este proyecto es la **optimización del ancho de banda y la precisión de la información**. 
La API original de Hipolabs entrega una gran cantidad de metadatos (dominios, códigos de país, estados/provincias, etc.) que pueden saturar al cliente final. 

**Nuestra intervención:**
1. **Filtrado Selectivo**: Mediante el uso de **DTOs (Data Transfer Objects)**, interceptamos la respuesta masiva y eliminamos los campos redundantes.
2. **Reducción de Carga**: Hemos recortado la respuesta en un **60% aproximadamente**, entregando únicamente lo esencial: el nombre de la institución y sus sitios web oficiales.
3. **Estandarización**: Garantizamos que cada objeto de la lista tenga una estructura predecible y limpia, facilitando su consumo en aplicaciones móviles o frontends modernos.

## 🏗️ Arquitectura de la Solución

El flujo de una petición sigue esta trayectoria lógica:
1. **Controller**: Recibe el parámetro `country` y coordina la ejecución.
2. **Service**: Capa intermedia que solicita los datos y ejecuta la **lógica de recorte y optimización**.
3. **Client**: Realiza la conexión `HTTPS` asíncrona mediante la librería `httpx`.
4. **DTO**: Define el contrato final de salida, asegurando la integridad de la respuesta optimizada.

## 📊 Comparativa de Datos

| Característica | API Original (Hipolabs) | Nuestra API (Optimizada) |
| :--- | :--- | :--- |
| **Campos devueltos** | `name`, `domains`, `web_pages`, `country`, `alpha_two_code`, `state-province` | `name`, `web_pages` |
| **Precisión** | Información bruta | Información filtrada y curada |
| **Peso de respuesta** | Alto (Datos redundantes) | Ligero (Solo datos útiles) |

## 🛠️ Stack Tecnológico
- **Lenguaje**: Python 3.10+
- **Framework**: FastAPI (ASGI)
- **Cliente HTTP**: Httpx (Async)
- **Validación**: Pydantic v2
- **Documentación**: Swagger / OpenAPI 3.0

## 🚀 Guía de Despliegue

1. **Entorno**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # Windows
