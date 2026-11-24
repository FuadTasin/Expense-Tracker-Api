from datetime import timedelta
from datetime import datetime,timezone
from typing import Annotated
from fastapi import Depends, HTTPException
from jose import JWTError, jwt
import os
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')
OAuth2_bearer=OAuth2PasswordBearer(tokenUrl='/auth/login')

def create_access_token(username:str,user_id,expire_delta:timedelta):
    encode={
        'sub':username,
        'id':user_id,
    }
    expire=datetime.now(timezone.utc)+expire_delta
    encode.update({
        'exp':expire
    })
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

def get_current_user(token:Annotated[str,Depends(OAuth2_bearer)]):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get('sub')
        user_id:int=payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=404,detail="User not found.")
        return{
            'username':username,
            'id':user_id
        }
    except JWTError:
        raise HTTPException(status_code=401,detail="Could not validate credentials")