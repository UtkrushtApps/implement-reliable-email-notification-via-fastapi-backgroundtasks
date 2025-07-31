from pydantic import BaseModel, EmailStr

class UserUpdate(BaseModel):
    email: EmailStr
    full_name: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
