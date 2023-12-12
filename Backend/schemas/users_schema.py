from pydantic import BaseModel, EmailStr as email, constr, field_validator, model_validator
from typing import Optional, Union
import re

class UserCreateSchema(BaseModel):
    username: constr(strip_whitespace=True, min_length=4, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    email: email
    password: constr(min_length=6)

    @classmethod
    @field_validator('password')
    def password_complexity(cls, value: str):
        if not re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]', value):
            raise ValueError(
                'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character')
        return value

class UserLoginSchema(BaseModel):
    username: Union[email, constr(min_length=3, max_length=20, pattern="^[a-zA-Z0-9_]+$")]
    password: str
    type: Optional[str] = None

    @model_validator(mode='after')
    def check_username_or_email(self):
        if "@" in self.username:
            self.type = "email"
        else:
            self.type = "username"

        return self
class UserUpdateSchema(BaseModel):
    username: str or None = None
    email: email or None = None
