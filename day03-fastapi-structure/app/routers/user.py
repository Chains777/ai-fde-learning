from fastapi import APIRouter

from app.models.user import User, UserResponse


router = APIRouter()


@router.post(
    "/users",
    response_model=UserResponse
)
def create_user(user: User):
    return {
    "message": "User created",
    "user": user,
}