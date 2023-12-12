from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from fastapi import APIRouter


class Database:
    client: AsyncIOMotorClient = None
    users: AsyncIOMotorCollection = None


db = Database()
db_router = APIRouter()


def get_database() -> Database:
    return db


@db_router.on_event("startup")
async def startup_db_client():
    db.client = AsyncIOMotorClient("mongodb://localhost:27017")
    db.users = db.client.survey_app.users


@db_router.on_event("shutdown")
async def shutdown_db_client():
    db.client.close()
