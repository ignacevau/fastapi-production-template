from typing import List

from fastapi import APIRouter, status

from .models import User
from .schemas import UserIn, UserOut

user = APIRouter(
    prefix="/users",
)


@user.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    description="Create a user",
)
async def create_user(user: UserIn):
    user = await User.create(**user.dict())
    return user


@user.get("/{id}", response_model=UserOut)
async def get_user(id: str):
    user = await User.get(id)
    return user


@user.get("/", response_model=List[UserOut])
async def get_all_users():
    users = await User.get_all()
    return users


@user.put("/{id}", response_model=UserOut)
async def update(id: str, user: UserIn):
    user = await User.update(id, **user.dict())
    return user


@user.delete("/{id}", response_model=bool)
async def delete_user(id: str):
    return await User.delete(id)
