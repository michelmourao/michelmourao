from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt
from app.auth import oauth2_scheme
from app.utils import SECRET_KEY, ALGORITHM
from datetime import datetime, timezone

router = APIRouter()

@router.get("/datetime")
def get_datetime():
    dt = datetime.now()
    return dt

@router.get("/hello")
def hello_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name = payload.get("sub")
        if user_name is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"message": f"Hello, {user_name}!"}