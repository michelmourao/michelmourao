import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "9uf309d039ue09u"
ALGORITHM = "HS256"

def create_jwt_token(username: str):
    payload = {
        "sub": username,
        "extra": 'Other useful information',
        "iat": datetime.now(tz=timezone.utc),
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=30) #or hours, days
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

sub = payload.get('sub')
iat = payload.get('iat')
exp = payload.get('exp')

seconds = exp - iat
minutes = seconds / 60
print(minutes)

#input()