from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from app.utils import SECRET_KEY, ALGORITHM, verify_password, create_access_token, get_password_hash
from app.models import UserCRUD
from app.database import session

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Rota para login
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Função para autenticar o usuário
def authenticate_user(username: str, password: str):
    
    user_crud = UserCRUD(session)
    user = user_crud.read_user(username=username)

    if user is not None:
        print(f"Usuário encontrado: {user.username}, hash: {user.password_hash}")
        passhash = user.password_hash
    else:
        print("Usuário não encontrado")
        return False
    session.close()

    verification = verify_password(password, passhash)
    print(f'Verification: {verification}')

    if verification is False:
        return False
    else:
        return user
