from fastapi import APIRouter , Depends
from database import get_db 
from typing import List
from services.create_category import create_category , get_categories
from sqlmodel import Session 
from schemas.schemas import CategoryCreate ,CategoryResponse
router=APIRouter(prefix="/categories" , tags=["Categories"])
@router.post("/" , response_model=CategoryResponse)
def create_new_category(category:CategoryCreate , db :Session =Depends(get_db)):
    return create_category(db=db , category = category)
@router.get("/" , response_model=List[CategoryResponse])
def read_categories(db:Session=Depends(get_db)):
    return get_categories(db=db)