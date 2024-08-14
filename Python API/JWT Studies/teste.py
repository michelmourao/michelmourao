import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

def create_jwt_token(username: str):
    payload = {
        "sub": username,
        "iat": datetime.now(tz=timezone.utc),
        "exp": datetime.utcnow() + timedelta(minutes=15)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def validate_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token expirado. Faça login novamente."
    except jwt.InvalidTokenError:
        return "Token inválido."

# Gerar o token
username = "user1"
token = create_jwt_token(username)
print(f"Token JWT Gerado: {token}")

# Validar o token
payload = validate_jwt_token(token)
print(f"Payload Decodificado: {payload}")
input()