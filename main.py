from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from sqlmodel import SQLModel
from routers import categorie, produit

# Création des tables SQLite au démarrage
SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="E-commerce SaaS Platform",
    description="Application Full-Stack E-commerce avec FastAPI, SQLModel & Jinja2/Tailwind",
    version="1.0.0"
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montage du dossier static (pour CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Déclaration du dossier des templates Jinja2
templates = Jinja2Templates(directory="templates")

# Inclusion des routeurs API REST
app.include_router(categorie.router)
app.include_router(produit.router)

# Route principale Web (Servie avec Jinja2 + Tailwind)
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"title": "Mauritania E-Commerce"}
    )