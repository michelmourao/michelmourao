#http://localhost:8000/docs
#http://localhost:8000/redoc

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import endpoints, users, systemprompts
from app.auth import router as auth_router

app = FastAPI(
    title="CRUD API",
    description="It's a service to create, read, update or delete users",
    version="1.0.0"
)

app = FastAPI()

# Configurando o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem. Substitua "*" por uma lista de domínios permitidos em produção.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


app.include_router(auth_router, tags=["Authentication"])
app.include_router(endpoints.router, prefix="/test", tags=["Test"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(systemprompts.router, prefix="/systemprompts", tags=["System Prompts"])
#app.include_router(items.router, prefix="/items", tags=["items"])