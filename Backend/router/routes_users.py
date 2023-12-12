import uuid

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
import schemas.users_schema as schema
import utils.utils as utils
import logging

logging.basicConfig(filename='app.log',
                    filemode='a',  # 'a' ??? ?????????? (append) ? ???????????? ?????, 'w' ??? ??????????
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # ?????? ????
                    level=logging.INFO)

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/register")
async def register_user(user_data: schema.UserCreateSchema):
    existing_user_by_email = await utils.fetch_user_by_email(user_data.email)
    if existing_user_by_email:
        raise HTTPException(status_code=400, detail="Email already in use")

    existing_user_by_username = await utils.fetch_user_by_username(user_data.username)
    if existing_user_by_username:
        raise HTTPException(status_code=400, detail="Username already in use")

    new_user = await utils.create_user(user_data)

    access_token_expires = timedelta(minutes=30)
    new_user_uid = uuid.UUID(bytes=new_user["uid"])
    access_jwt_token = utils.create_access_token(
        data={"sub": str(new_user_uid)}, expires_delta=access_token_expires
    )

    return {"message": "User registered successfully", "access_token": access_jwt_token, "token_type": "bearer"}

@router.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    credentials = schema.UserLoginSchema(username=form_data.username, password=form_data.password)

    if credentials.type == "email":
        user = await utils.fetch_user_by_email(credentials.username)
    else:
        user = await utils.fetch_user_by_username(credentials.username)

    if not user or not utils.verify_password(credentials.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail=f"Incorrect credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = utils.create_access_token(
        data={"sub": str(uuid.UUID(bytes=user["uid"]))},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
async def get_current_user():
    return {"user": "get current_user data"}

@router.put("/me")
async def update_user(user_update: schema.UserUpdateSchema):
    return {"user": "User update successfully"}
