from fastapi import APIRouter, Depends, HTTPException, status
from jose import JWTError, jwt
from app.auth import oauth2_scheme
from app.utils import SECRET_KEY, ALGORITHM
from app.models import User
from app.models import UserCRUD
from app.database import session

router = APIRouter()

@router.get("/{user_id}")
async def get_user_endpoint(user_id: int):

    user_crud = UserCRUD(session)
    user = user_crud.read_user(user_id=user_id)
    session.close()

    if user is not None:
        print(f"Usuário encontrado: {user.username}")
        return user
    else:
        print("Usuário não encontrado")
        raise HTTPException(status_code=404, detail="User not found")
    
    #falta ocultar o hash no retorno e poteger o endpoint.