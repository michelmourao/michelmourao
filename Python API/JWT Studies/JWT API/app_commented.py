from fastapi import FastAPI, Depends, HTTPException, status
#     FastAPI: Cria uma aplicação FastAPI.
#     Depends: Define dependências para rotas, permitindo injeção de dependências.
#     HTTPException: Lança exceções HTTP personalizadas.
#     status: Fornece códigos de status HTTP, como status.HTTP_401_UNAUTHORIZED.

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#     OAuth2PasswordBearer: Implementa o fluxo de senha OAuth2 para obtenção do token JWT.
#     OAuth2PasswordRequestForm: Representa o formulário de login com username e password.

from datetime import datetime, timedelta
#     datetime: Manipula datas e horas.
#     timedelta: Manipula intervalos de tempo, usado aqui para definir expiração do token.

import jwt
#     jwt: Importa a biblioteca PyJWT para manipulação de JSON Web Tokens.

app = FastAPI() # Cria uma instância da aplicação FastAPI, que será usada para definir rotas e configurar a API.

SECRET_KEY = "joids89d9as8da9s8da9s8d7a9123dg1f33f3fsss8d022sss2222s" # Define a chave secreta usada para assinar o JWT. É fundamental que essa chave seja segura e protegida, pois qualquer pessoa com acesso a essa chave pode gerar tokens válidos.
ALGORITHM = "HS256" # Define o algoritmo de criptografia usado para assinar o JWT. O HS256 é o algoritmo HMAC com SHA-256.
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # Define o tempo de expiração do token em minutos. Neste caso, o token será válido por 30 minutos.

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    # Cria um esquema de autenticação OAuth2 do tipo PasswordBearer.
    # tokenUrl="token" indica que a rota que gerará os tokens JWT é a rota /token.
    # Esse esquema é usado como uma dependência em rotas que requerem autenticação.

def create_access_token(data: dict): # Define uma função que cria um token JWT. Recebe um dicionário (data) que representa as claims (informações) que serão codificadas no token.
    to_encode = data.copy() # Faz uma cópia dos dados fornecidos para evitar modificar o dicionário original.
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) 
        # Calcula a data de expiração do token adicionando o tempo de expiração atual (ACCESS_TOKEN_EXPIRE_MINUTES) ao tempo atual (datetime.utcnow()).
        # datetime.utcnow() retorna o horário UTC atual.
        # timedelta(minutes=...) adiciona a quantidade de minutos definida à data/hora atual.
    to_encode.update({"exp": expire}) # Adiciona uma nova chave exp ao dicionário to_encode, onde exp representa a data/hora de expiração do token.
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        # Usa a função jwt.encode para gerar o token JWT.
        # to_encode: O dicionário com as informações (claims) a serem codificadas.
        # SECRET_KEY: A chave secreta usada para assinar o token.
        # algorithm=ALGORITHM: O algoritmo de criptografia escolhido.
    return encoded_jwt # Retorna o token JWT gerado.


@app.post("/token") # Define uma rota HTTP POST na URL /token. Esta rota será usada para gerar e retornar um token JWT.
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Define uma função assíncrona login para a rota /token.
    # form_data: OAuth2PasswordRequestForm = Depends(): Extrai o formulário de login usando OAuth2PasswordRequestForm. O Depends() é usado para declarar uma dependência, que automaticamente carrega e valida os dados do formulário de login.
    user_dict = {"sub": form_data.username} # Cria um dicionário user_dict com a chave sub (subject), que armazena o nome de usuário extraído do formulário.
    access_token = create_access_token(data=user_dict) # Chama a função create_access_token para gerar o token JWT, passando user_dict como as claims do token.
    return {"access_token": access_token, "token_type": "bearer"} # Retorna o token JWT gerado como um dicionário JSON com as chaves access_token e token_type. O tipo de token é especificado como bearer.
    
# Define uma rota HTTP GET na URL '/users/me', que retorna as informações do usuário autenticado.
# Esta rota está protegida e requer que um token JWT válido seja fornecido para acesso.
@app.get("/users/me")
# Função assíncrona que obtém as informações do usuário autenticado.
# O token JWT é extraído automaticamente do cabeçalho da solicitação usando o esquema 'oauth2_scheme'.
# A função 'Depends' injeta o token JWT diretamente na função como o parâmetro 'token'.
async def read_users_me(token: str = Depends(oauth2_scheme)):
    # Cria uma exceção personalizada para lidar com erros de autenticação.
    # Essa exceção será lançada se o token não puder ser validado.
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,  # Define o código de status HTTP como 401 Unauthorized.
        detail="Could not validate credentials",  # Mensagem detalhada sobre a falha na autenticação.
        headers={"WWW-Authenticate": "Bearer"},  # Cabeçalho que indica o tipo de autenticação exigida (Bearer).
    )

    try:
        # Decodifica o token JWT para extrair o payload.
        # A decodificação falhará se o token for inválido ou se a assinatura não coincidir com a 'SECRET_KEY' usada para assiná-lo.
        # 'payload' é um dicionário que contém as claims codificadas no token.
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Extrai o nome de usuário do payload do token.
        # A claim 'sub' deve conter o nome de usuário do sujeito (subject) do token.
        username: str = payload.get("sub")

        # Se o nome de usuário não estiver presente no payload, lança a exceção de credenciais inválidas.
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        # Se ocorrer qualquer erro durante a decodificação do token JWT (ex: token expirado, assinatura inválida),
        # a exceção é capturada e a exceção de credenciais inválidas é lançada.
        raise credentials_exception

    # Se o token JWT for válido e o nome de usuário estiver presente no payload,
    # a função retorna um dicionário JSON contendo o nome de usuário.
    return {"username": username}