from fastapi import FastAPI
from app.endpoints import endpoints, users
from app.auth import router as auth_router
from datetime import datetime, timezone

app = FastAPI()

app.include_router(auth_router)
app.include_router(endpoints.router, prefix="/protected", tags=["protected"])
app.include_router(users.router, prefix="/users", tags=["Users"])
#app.include_router(items.router, prefix="/items", tags=["items"])

@app.get("/datetime")
def get_datetime():
    dt = datetime.now()
    return dt