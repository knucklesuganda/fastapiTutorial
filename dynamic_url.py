from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    username: str
    email: str
    password: str


@app.post("/create_user")
def create_user_route(new_user: User):
    users.append(new_user)
    return {
        "created": True,
    }


@app.get("/users")
def get_all_users():
    return {
        "users": users,
    }


@app.get("/users/{user_id}")
def get_user_route(user_id: int):
    return users[user_id]
