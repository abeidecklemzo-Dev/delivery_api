from sqlmodel import SQLModel , Field 
from typing import Optional 
class Product(SQLModel , table =True):
    __tablename__="Produits"
    id : Optional[int]=Field(default=None ,primary_key=True)
    name : str =Field( index =True )
    description : Optional [str] =Field(default=None)
    price : float
    stock : int =Field(default=0)
    