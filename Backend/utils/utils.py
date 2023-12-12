import base64
import json

from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from Database.database_utils import get_database
from bson.binary import Binary as binary
import uuid


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "secret-key"
ALGORITHM = "HS256"

async def fetch_user_by_email(email: str):
    user = await get_database().users.find_one({"email": email}, {"uid": 1, "hashed_password": 1})
    return user

async def fetch_user_by_username(username: str):
    user = await get_database().users.find_one({"username": username}, {"uid": 1, "hashed_password": 1})
    return user

async def hash_password(password: str):
    return pwd_context.hash(password)

async def veryfi_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def create_user(user_data):
    hashed_password = await hash_password(user_data.password)
    user_id = binary.from_uuid(uuid.uuid4())
    new_user = {**user_data.dict(), "hashed_password": hashed_password, "uid": user_id}
    new_user.pop("password", None)
    await get_database().users.insert_one(new_user)
    new_user.pop("hashed_password", None)
    return new_user

async def get_user(email):
    user = await get_database().users.find_one({"email": email})
    return user

async def update_user(email, user_update_data):
    await get_database().users.update_one({"email": email}, {"set": user_update_data})
    return await get_user(email)

async def delete_user(email):
    await get_database().users.delete_one({"email": email})
    return {"username": "User deleted"}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    payload = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, SECRET_KEY, ALGORITHM)

    return encoded_jwt


