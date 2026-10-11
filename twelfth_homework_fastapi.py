from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

users = [
    {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "age": 25},
    {"id": 2, "name": "Bob Johnson", "email": "bob@example.com", "age": 30},
    {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com", "age": 22},
]


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int


app = FastAPI()


@app.get("/users")
async def get_users():
    return users


@app.get("/users/{user_id}", response_model=User)
async def find_user(user_id: int) -> dict:
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="User with this ID not found"
    )


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def user_create(user: UserCreate):
    new_user = {"id": len(users) + 1, **user.model_dump()}
    users.append(new_user)
    return {"message": "User was successfully created", "user": new_user}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int) -> dict[str, str]:
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User was deleted"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="User with this ID not found"
    )
