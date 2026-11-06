from fastapi import APIRouter , Depends 
from database import get_db
from sqlmodel import Session
from typing import List
from services.create_product import get_product, create_product
from schemas.schemas import ProductCreate , ProductResponse
router=APIRouter(prefix="/produits" , tags=["Produits"])
@router.post("/" , response_model=ProductResponse)
def create_new_produit(product:ProductCreate ,db :Session=Depends(get_db)):
    return create_product(db=db , product=product)
@router.get("/" , response_model=List[ProductResponse])
def get_new_product(db:Session = Depends(get_db)):
    return get_product(db=db)