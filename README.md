# 🚀 FastAPI Modular E-Commerce API

API REST modulaire et performante développée avec **FastAPI**, **SQLModel** et **SQLite**, conçue selon les principes de l'architecture propre (Separation of Concerns). Ce projet sert de backend robuste pour des applications e-commerce et des solutions de gestion de stock, ciblant notamment la digitalisation des commerces locaux.

## 🛠️ Stack Technique

* **Framework :** FastAPI (Python)
* **ORM & Base de données :** SQLModel / SQLite
* **Validation des données :** Pydantic v2
* **Architecture :** Modulaire (Séparation des routes, services, modèles et schémas)

## 📂 Structure du Projet

```text
.
├── database.py         # Configuration de la connexion et session BDD
├── models.py           # Modèles SQLModel (Tables: Category, Product)
├── schemas.py          # Schémas Pydantic (Entrées et Sorties)
├── services.py         # Logique métier et interactions CRUD
├── routers/
│   ├── categories.py   # Endpoints REST pour les catégories
│   └── produits.py     # Endpoints REST pour les produits
└── main.py             # Point d'entrée de l'application FastAPI