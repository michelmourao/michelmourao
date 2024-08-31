#http://localhost:8000/docs
#http://localhost:8000/redoc

from fastapi import FastAPI
from app.endpoints import endpoints, users
from app.auth import router as auth_router

app = FastAPI(
    title="CRUD API",
    description="It's a service to create, read, update or delete users",
    version="1.0.0"
)

#app.include_router(auth_router)
app.include_router(auth_router, tags=["Authentication"])
app.include_router(endpoints.router, prefix="/test", tags=["Test"])
app.include_router(users.router, prefix="/users", tags=["Users"])
#app.include_router(items.router, prefix="/items", tags=["items"])