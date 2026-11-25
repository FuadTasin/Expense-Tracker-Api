from pydantic import BaseModel, EmailStr,Field
from typing import Annotated, Literal,Optional


class UserRegistration(BaseModel):
    username:Annotated[str,Field(...,description="Username")]
    email:Annotated[EmailStr,Field(...,description="Email")]
    password:Annotated[str,Field(...,description="Password")]

class CreateTransaction(BaseModel):
    id:Annotated[int,Field(...,description='Transaction Id')]
    title:Annotated[str,Field(...,description='Transaction title')]
    amount:Annotated[float,Field(...,gt=0,description='Transaction amount')]
    type:Literal['income','expense']
    category:Annotated[str,Field(...,description='Transaction category')]

class UpdateTransaction(BaseModel):
    title:Annotated[Optional[str],Field(description='Transaction title',default=None)]
    amount:Annotated[Optional[float],Field(description='Transaction amount',default=None)]
    type:Annotated[Optional[Literal['income','expense']],Field(description='Transaction Type',default=None)]
    category:Annotated[Optional[str],Field(description='Transaction category',default=None)]