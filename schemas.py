from pydantic import BaseModel, EmailStr,Field
from typing import Annotated,Optional

class UserRegistration(BaseModel):
    username:Annotated[str,Field(...,description="Username")]
    email:Annotated[EmailStr,Field(...,description="Email")]
    password:Annotated[str,Field(...,description="Password")]

class CreateTransaction(BaseModel):
    id:Annotated[int,Field(...,description='Transaction Id')]
    title:Annotated[str,Field(...,description='Transaction title')]
    amount:Annotated[float,Field(...,description='Transaction amount')]
    type:Annotated[str,Field(...,description='Income/Expense')]
    category:Annotated[str,Field(...,description='Transaction category')]

class UpdateTransaction(BaseModel):
    title:Annotated[Optional[str],Field(description='Transaction title',default=None)]
    amount:Annotated[float,Field(description='Transaction amount',default=None)]
    type:Annotated[str,Field(description='Income/Expense',default=None)]
    category:Annotated[str,Field(description='Transaction category',default=None)]