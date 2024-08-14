from fastapi import FastAPI
from auth import router as auth_router
from datetime import datetime

app = FastAPI()

app.include_router(auth_router)

@app.get("/datetime")
def get_datetime():
    dt = datetime.now()
    return dt
