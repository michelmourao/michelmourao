from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import secrets

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Contexto para hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para criar o token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para verificar a senha
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para gerar o hash da senha
def get_password_hash(password):
    return pwd_context.hash(password)

# Função para verificar o token
def token_verification(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        print(f"Token verification log - Email: {email}")

        if email is None:
            return None
        
        return email
    
    except:
        return None

# Função para extrair o user_id do token - Como tinha muito código implementado retornando apenas o email na token_verification. Resolvi não alterar para uma tupla.
def collect_id(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        print(f"Token verification log - Id: {user_id}")

        if user_id is None:
            return None
        
        return user_id
    
    except:
        return None