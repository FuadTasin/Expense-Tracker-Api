from fastapi import FastAPI
from database import engine
import models
from router import authentication
import transactions

app=FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(authentication.router)
app.include_router(transactions.router)
