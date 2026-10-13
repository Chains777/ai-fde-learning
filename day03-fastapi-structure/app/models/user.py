from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    message: str
    user: User