# 🚀 Express Store - SaaS E-Commerce Platform

Plateforme e-commerce Full-Stack moderne conçue pour le marché local et régional, développée avec une architecture propre et des technologies de pointe.

## 🛠️ Stack Technique

* **Backend** : FastAPI (Python)
* **Base de données & ORM** : SQLite & SQLModel
* **Moteur de Templates** : Jinja2 (Server-Side Rendering)
* **Design & UI** : Tailwind CSS (Mode Sombre / Dark Mode)
* **Serveur ASGI** : Uvicorn

## 📂 Structure du Projet

```text
express-store-saas/
├── main.py              # Point d'entrée FastAPI & configuration Jinja2/Static
├── database.py          # Configuration de la base de données SQLite
├── models.py            # Modèles SQLModel (Produits, Catégories)
├── schemas.py           # Schémas Pydantic pour la validation
├── services/            # Logique métier et interactions avec la base de données
├── routers/             # Routeurs API REST (Produits, Catégories)
├── templates/           # Fichiers HTML Jinja2 (base.html, index.html)
└── static/              # Fichiers statiques (CSS, JS, Images)