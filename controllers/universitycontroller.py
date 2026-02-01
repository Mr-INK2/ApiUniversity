import httpx
from fastapi import APIRouter
from typing import List
from services.universityService import UniversityService
from DTOs.universityDtos import UniversityResponseDTO

router = APIRouter(prefix="/api")

@router.get("/universities/{country}", response_model=List[UniversityResponseDTO])
async def get_universities(country: str):
    
    async with httpx.AsyncClient() as http_client:
        university_service = UniversityService()
        universities_response = await university_service.get_universities(country, http_client)
        return universities_response