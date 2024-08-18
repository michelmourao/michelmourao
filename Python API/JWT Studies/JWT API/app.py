from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta, timezone
import jwt

# Crie uma instância do FastAPI
app = FastAPI(
    title="My study API",
    description="For authenticate remember to send the credentials on request body.",
    version="1.0.1",
    openapi_tags=[{"name": "auth", "description": "Authentication endpoints"}],
    swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
    swagger_ui_init_oauth={
        "clientId": "your-client-id",
        "clientSecret": "your-client-secret",
    },
 )

# Defina uma chave secreta (deve ser mantida em segredo)
SECRET_KEY = "secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração do OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Rota para geração de token
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    # Aqui você faria a verificação do usuário, etc.
    user_dict = {"sub": form_data.username} 
    print(f'Username: {form_data.username}, Pwd: {form_data.password}, Cid: {form_data.client_id}, Csecret: {form_data.client_secret}')
    
    if not form_data.client_id or not form_data.client_secret:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Client ID and Client Secret must not be empty",
        )
    access_token = create_access_token(data=user_dict)
    return {"access_token": access_token, "token_type": "bearer"}

# Rota protegida que exige um token JWT
@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    return {"username": username}

@app.get("/datetime")
async def getdatetime():
    date_time =  datetime.now(tz=timezone.utc)
    date_time_str = date_time.isoformat()
    return date_time_str