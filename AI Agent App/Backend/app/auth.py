from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.utils import verify_password, create_access_token
from app.models import UserModel
from app.database import session

UserCRUD = UserModel.UserCRUD

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Rota para login
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"email": user.email, "user_id": user.id })
    return {"access_token": access_token, "token_type": "bearer"}

# Função para autenticar o usuário
def authenticate_user(email: str, password: str):
    
    user_crud = UserCRUD(session)
    user = user_crud.read_user(email=email)

    if user is not None:
        print(f"Usuário encontrado: {user.email}, hash: {user.pswd}")
        passhash = user.pswd
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
