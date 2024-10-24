from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    firstName: str
    lastName: str
    age: int
    emailId: EmailStr
    password: str
    address: str
    state: str
    pinCode: int

class UserLogin(BaseModel):
    emailId: EmailStr
    password: str
