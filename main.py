from fastapi import FastAPI
from database import engine
from models import SQLModel
from routers import categorie , produit
SQLModel.metadata.create_all(engine)
app = FastAPI(
    title="E-commerce API",
    description="API REST modulaire pour la gestion de produits et catégories",
    version="1.0.0"
)
app.include_router(categorie.router)
app.include_router(produit.router)
@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API E-commerce !"}

