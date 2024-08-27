from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt
from app.auth import oauth2_scheme
from app.utils import SECRET_KEY, ALGORITHM
from app.models import UserCRUD, UserResponse, User
from app.database import session

router = APIRouter()

async def get_user_endpoint(user_id: int, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name = payload.get("sub")
        if user_name is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user_crud = UserCRUD(session)
    user = user_crud.read_user(user_id=user_id)
    session.close()

    if user is not None:
        print(f"Usuário encontrado: {user.username}")
        return user
    else:
        print("Usuário não encontrado")
        raise HTTPException(status_code=404, detail="User not found")


@router.get("/{user_id}", response_model=UserResponse)

async def read_users(user = Depends(get_user_endpoint)):
    return user