"""API du portail de l'Université Anjombakilala d'Androy (UAA).

Toutes les routes sont servies sous /api : le futur front (uaa-portal-web) occupera la racine du site.
"""
from fastapi import APIRouter, FastAPI

app = FastAPI(title="UAA - API du portail", docs_url="/api/docs", openapi_url="/api/openapi.json")
api = APIRouter(prefix="/api")


@api.get("/")
def accueil():
    return {"service": "uaa-portal-api", "message": "Bonjour depuis la plateforme GitOps de l'Université d'Androy"}


@api.get("/health")
def sante():
    return {"status": "ok"}


app.include_router(api)
