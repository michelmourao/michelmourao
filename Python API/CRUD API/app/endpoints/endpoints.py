from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt
from app.auth import oauth2_scheme
from app.utils import SECRET_KEY, ALGORITHM

router = APIRouter()

# Rota protegida
@router.get("/protected")
def read_protected_data(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return {"message": f"Hello, {username}!"}