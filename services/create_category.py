from schemas.schemas  import CategoryCreate 
from models import Category , Product
from sqlmodel import Session , select
def create_category(db : Session , category:CategoryCreate):
    categorie=Category.model_validate(category)
    db.add(categorie)
    db.commit()
    db.refresh(categorie)
    return categorie

def get_categories(db:Session):
    statement=select(Category)
    return db.exec(statement).all() 

