from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import User, Task
from app.schemas.user import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])

@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars((select(User))).all()
    if users is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no users'
        )
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    return user

@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    tasks = db.scalar(select(Task).where(Task.user_id == user_id))
    if tasks is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'There are no tasks assigned on {user_id}'
        )
    return tasks

@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int):
    user_update = db.scalar(select(User).where(User.id == user_id))
    if user_update is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(update(User).where(User.id == user_id).values(# username=update_user.username,
                                                             firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful'
    }


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user_delete = db.scalar(select(User).where(User.id == user_id))
    if user_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    db.execute(delete(Task).where(Task.user_id == user_id))

    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User delete is successful'
    }
