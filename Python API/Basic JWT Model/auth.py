from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from utils import SECRET_KEY, ALGORITHM, verify_password, create_access_token, get_password_hash

router = APIRouter()

# Simulação de banco de dados em memória
fake_users_db = {
    "user1": {
        "username": "user1",
        "password": get_password_hash("password1"),  # Gera o hash da senha
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Rota para login
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user['username']})
    return {"access_token": access_token, "token_type": "bearer"}

# Função para autenticar o usuário
def authenticate_user(fake_db, username: str, password: str):
    user = fake_db.get(username)
    if not user or not verify_password(password, user["password"]):
        return False
    return user

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
