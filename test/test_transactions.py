from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from database import SessionLocal
from models import Todos
from test.test_main import client
from main import app
from fastapi import status
from router.tokens import get_current_user
from datetime import datetime,timezone

def override_get_current_user():
    return {
        'id':1,
        'username':'testuser'
    }

def test_transaction():
    db=SessionLocal()
    db.query(Todos).filter(Todos.id==99).delete()
    transaction=Todos(
        id=99,
        title='Testing',
        amount=1000,
        type="expenses",
        category="Food",
        date=datetime.now(timezone.utc),
        owner_id=1
    )
    db.add(transaction)
    db.commit()




app.dependency_overrides[get_current_user]=override_get_current_user


def test_get_all_transactions():
    response=client.get('/transactions')
    assert response.status_code==status.HTTP_200_OK


def test_get_specific_transaction():
    response=client.get('/transactions/99')
    assert response.status_code==HTTP_200_OK


def test_create_transaction():
    db=SessionLocal()
    db.query(Todos).filter(Todos.id==1).delete()
    db.commit()

    request_data={ 
        "id": 1,
        "title": "shopping",
        "amount": 100,
        "type": "expenses",
        "category": "Food"
    }
    response=client.post('/transactions/create',json=request_data)
    assert response.status_code==HTTP_201_CREATED
    assert response.json()=={'message':'Transaction created successfully.'}


def test_update_transaction():
    request_data={ 
        "amount": 669,
        "type": "income",
    }
    response=client.put('/transactions/update/1',json=request_data)
    assert response.status_code==HTTP_200_OK
    assert response.json()=={'message':'Transaction updated successfully.'}


def test_delete_transaction():
    response=client.delete('/transactions/delete/1')
    assert response.status_code==HTTP_200_OK
    assert response.json()=={'message':'Transaction deleted successfully.'}
