from fastapi import APIRouter

survey_router = APIRouter()

@survey_router.get("/surveys")
async def read_surveys():
    return {"message": "List of surveys"}

