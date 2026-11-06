from sqlmodel import SQLModel , Field 
from typing import Optional
class Category (SQLModel , table = True):
    __tablename__= "catégotries" 
    id : Optional[int]=Field(default = None , primary_key =True)
    name: str =Field(unique=True , index = True )
    description :Optional[str] =Field(default=None)