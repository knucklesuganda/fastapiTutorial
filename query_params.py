from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserSchema(BaseModel):
    id: int
    username: str


class FullUserSchema(UserSchema):
    email: str
    balance: float


users = [
    FullUserSchema(
        id=0,
        username="Andrey",
        email="python.on.papyrus@gmail.com",
        balance=100000000,
    ),
    FullUserSchema(
        id=1,
        username="Test",
        email="test@gmail.com",
        balance=12345,
    ),
]


@app.get('/users/{id}/')
def get_user_route(id: int, is_admin: bool = False):
    if is_admin:
        return users[id]

    return UserSchema(
        id=users[id].id,
        username=users[id].username,
    )
