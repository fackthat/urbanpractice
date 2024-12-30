from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {
    '1': 'Имя: Кирилл, возраст: 33',
    '2': 'Имя: Алексей, возраст: 28'
}


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}

@app.get('/users')
async def get_all_users():
    return users

@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=2,
                                      max_length=20,
                                      description='Enter username',
                                      example='UrbanUser')],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description='Enter age',
                                 example=24)]
):
    new_id = str(max(map(int, users.keys())) + 1) if users else "1"
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return {"message": f"User {new_id} is registered"}

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[str, 'ID of the user to update'],
        username: Annotated[str, Path(min_length=2,
                                      max_length=20,
                                      description='Enter username',
                                      example='UrbanUser')],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description='Enter age',
                                 example=24)]
):
    if user_id not in users:
        return {'error': 'User not found'}
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return {'message': f'The user {user_id} is updated successfully'}

@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[str, Path(
            description='ID of the user to delete')]
):
    if user_id not in users:
        return {'error': 'User not found'}
    users.pop(user_id)
    return {'message': f'User {user_id} has been deleted'}
