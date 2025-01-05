from fastapi import FastAPI, Path, status, Body, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users_list": users})

@app.get('/user/{user_id}')
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.post('/')
async def create_user(
        username: Annotated[str, Form(min_length=2,
                                      max_length=20,
                                      description='Enter username',
                                      example='UrbanUser')],
        age: Annotated[int, Form(ge=18,
                                 le=120,
                                 description='Enter age',
                                 example=24)]
):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return templates.TemplateResponse("users.html", {"request": {}, "users_list": users})

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, 'ID of the user to update'],
        username: Annotated[str, Path(min_length=2,
                                      max_length=20,
                                      description='Enter username',
                                      example='UrbanUser')],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description='Enter age',
                                 example=24)]
):
    for existing_user in users:
        if existing_user.id == user_id:
            existing_user.username = username
            existing_user.age = age
            return existing_user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(
            description='ID of the user to delete')]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
