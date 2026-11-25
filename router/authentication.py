from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter,HTTPException,Depends
from fastapi.responses import JSONResponse
from dependencies import db_dependency
from router.tokens import create_access_token
from schemas import UserRegistration
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from models import Users

router=APIRouter()

bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')

def authentiate_user(username,password,db):
    user=db.query(Users).filter(Users.username==username).first()
    if user is None:
        return False
    if bcrypt_context.verify(password,user.hash_password):
        return user
    else:
        return False


@router.post('/auth/register')
def user_registration(db:db_dependency,user:UserRegistration):
    check_user=db.query(Users).filter(Users.username==user.username).first()
    if check_user is not None:
        raise HTTPException(status_code=404,detail='Username/Email already exist.')
    new_user=Users(
        username=user.username,
        email=user.email,
        hash_password=bcrypt_context.hash(user.password)
    )
    db.add(new_user)
    db.commit()

    return JSONResponse(status_code=201,content='User created successfully.')


@router.post('/auth/login')
def user_login(db:db_dependency,form_user:Annotated[OAuth2PasswordRequestForm,Depends()]):
    user=authentiate_user(form_user.username,form_user.password,db)
    if not user:
        raise HTTPException(status_code=404,detail='Failed Login.')
    token=create_access_token(user.username,user.id,timedelta(minutes=30))
    return {
        'access_token':token,
        'token_type':'bearer'
    }