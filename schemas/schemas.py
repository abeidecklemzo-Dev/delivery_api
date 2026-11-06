from pydantic import BaseModel
from typing import Optional
class CategoryCreate(BaseModel):
    name : str
    description : Optional[str]=None
class CategoryResponse(BaseModel):
    id : int
    name : str
    description :Optional[str]=None  
    model_config = {"from_attributes": True}  
class ProductCreate(BaseModel):
    name :str
    description :Optional[str]=None
    price : float
    stock :Optional[int] =0  
class ProductResponse(BaseModel):
    id : int
    name :str
    description:Optional[str]=None
    price : float
    stock :Optional[int]=0     