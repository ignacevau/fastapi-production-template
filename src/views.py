from typing import List

from fastapi import APIRouter, status
from pydantic import BaseModel

from src.models import User


class UserSchema(BaseModel):
    full_name: str


class UserSerializer(BaseModel):
    id: str
    full_name: str

    class Config:
        orm_mode = True


api = APIRouter(
    prefix="/users",
)


@api.post(
    "/", 
    response_model=UserSerializer,
    status_code=status.HTTP_201_CREATED,
    description="Create a user",
)
async def create_user(user: UserSchema):
    user = await User.create(**user.dict())
    return user


@api.get("/{id}", response_model=UserSerializer)
async def get_user(id: str):
    user = await User.get(id)
    return user


@api.get("/", response_model=List[UserSerializer])
async def get_all_users():
    users = await User.get_all()
    return users


@api.put("/{id}", response_model=UserSerializer)
async def update(id: str, user: UserSchema):
    user = await User.update(id, **user.dict())
    return user


@api.delete("/{id}", response_model=bool)
async def delete_user(id: str):
    return await User.delete(id)
