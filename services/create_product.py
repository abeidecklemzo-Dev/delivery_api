from sqlmodel import Session , select
from models import Product
from schemas.schemas import ProductCreate
def create_product(db:Session , product:ProductCreate):
    produits=Product.model_validate(product)
    db.add(produits) 
    db.commit()
    db.refresh(produits)
    return produits

def get_product(db : Session):
    statement=select(Product)
    return db.exec(statement).all()
 