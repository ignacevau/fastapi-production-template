from pydantic import BaseModel


class UserOut(BaseModel):
    id: str
    full_name: str

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    full_name: str
