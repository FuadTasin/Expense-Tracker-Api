from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from dependencies import db_dependency, user_dependency
from models import Todos
from schemas import CreateTransaction, UpdateTransaction
from datetime import datetime,timezone

router=APIRouter()

@router.get('/transactions')
def get_all_transactions(user:user_dependency,db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401,detail='Failed Authentication.')

    return db.query(Todos).filter(Todos.owner_id==user.get('id')).all()

@router.get('/transactions/{transaction_id}')
def get_specific_transaction(user:user_dependency,db:db_dependency,transaction_id:int):
    if user is None:
        raise HTTPException(status_code=401,detail='Failed Authentication.')

    todo=db.query(Todos).filter(Todos.owner_id==user.get('id')).filter(Todos.id==transaction_id).first()
    if todo is None:
        raise HTTPException(status_code=404,detail='Invalid Transaction Id.')
    return todo

@router.post('/transactions/create')
def create_transaction(user:user_dependency,db:db_dependency,transaction:CreateTransaction):
    if user is None:
        raise HTTPException(status_code=401,detail='Failed Authentication.')
    if db.query(Todos).filter(Todos.owner_id==user.get('id')).filter(Todos.id==transaction.id).first() is not None:
        raise HTTPException(status_code=404,detail='Transaction Id already exist.')
    new_transaction=Todos(
        id=transaction.id,
        title=transaction.title,
        amount=transaction.amount,
        type=transaction.type,
        category=transaction.category,
        date=datetime.now(timezone.utc),
        owner_id=user.get('id')
    )
    db.add(new_transaction)
    db.commit()
    return JSONResponse(status_code=201,content={'message':'Transaction created successfully.'})

@router.put('/transactions/update/{transaction_id}')
def update_transaction(user:user_dependency,db:db_dependency,transaction_id:int,transaction:UpdateTransaction):
    if user is None:
        raise HTTPException(status_code=401,detail='Failed Authentication.')
    
    update_transaction=db.query(Todos).filter(Todos.owner_id==user.get('id')).filter(Todos.id==transaction_id).first()
    if update_transaction is None:
        raise HTTPException(status_code=404,detail="Transaction not found.")
    
    update_data=transaction.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        setattr(update_transaction,key,value)
    db.commit()
    return JSONResponse(status_code=200,content={'message':'Transaction updated successfully.'})

@router.delete('/transactions/delete/{transaction_id}')
def delete_transaction(user:user_dependency,db:db_dependency,transaction_id:int):
    if user is None:
        raise HTTPException(status_code=401,detail='Failed Authentication.')
    if db.query(Todos).filter(Todos.owner_id==user.get('id')).filter(Todos.id==transaction_id).first() is None:
        raise HTTPException(status_code=404,detail="Transaction not found.")
    db.query(Todos).filter(Todos.owner_id==user.get('id')).filter(Todos.id==transaction_id).delete()
    db.commit()
    return JSONResponse(status_code=200,content={'message':'Transaction deleted successfully.'})

@router.get('/transactions/filter')
def filter_transactions(user:user_dependency,db:db_dependency,type:str=Query(...,description='Filter based on expenses'),category:str=Query(...,description='Filter based on Food'),min_amount:float=Query(default=None),max_amount:float=Query(default=None)):
    if user is None:
        raise HTTPException(status_code=401,detail='Failed Authentication.')
    type_field=["expenses"]
    category_field=["Food"]
    if type not in type_field or category not in category_field:
        raise HTTPException(status_code=404,detail="Invalid type/category")
    filtered_transaction=db.query(Todos).filter(Todos.owner_id==user.get('id')).filter(Todos.type==type).filter(Todos.category==category)
    if min_amount is not None:
        filtered_transaction=filtered_transaction.filter(Todos.amount>=min_amount)
    if max_amount is not None:
        filtered_transaction=filtered_transaction.filter(Todos.amount<=max_amount)
    return filtered_transaction.all()


    