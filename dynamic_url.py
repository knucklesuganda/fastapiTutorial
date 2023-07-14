from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
users = []


class User(BaseModel):
    email: str
    username: str
    password: str


@app.post("/")
def create_user(data: User):
    users.append(data)
    return {"created": True}


@app.get("/")
def get_users():
    return users


@app.get("/{id}")
def get_user_by_id(id: int):
    return users[id]
