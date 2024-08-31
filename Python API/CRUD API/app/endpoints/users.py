from fastapi import APIRouter, Depends, HTTPException, status, Body
from app.auth import oauth2_scheme
from app.utils import token_verification
from app.models import UserCRUD, UserResponse, UserCreate, UserUpdate
from app.database import session

router = APIRouter()

async def get_user_endpoint(user_id: int, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    user_name = token_verification(token)
    if user_name is None:
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


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)

async def create_user(user: UserCreate = Body(...), token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    user_name = token_verification(token)
    if user_name is None:
        raise credentials_exception
    
    # Verifica se email está em uso
    existing_user = UserCRUD(session).read_user(email=user.email)
    if existing_user:
        session.close()
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Verifica se username está em uso
    existing_user = UserCRUD(session).read_user(username=user.username)
    if existing_user:
        session.close()
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = UserCRUD(session).create_user(username=user.username, email=user.email, password=user.password)
    session.close()
    print('New user created!')

    return new_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_user(user_id: int, token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    user_name = token_verification(token)
    if user_name is None:
        raise credentials_exception

    #verifica se o usuário existe
    user_crud = UserCRUD(session)
    existing_user = user_crud.read_user(user_id=user_id)
    print(existing_user)

    if existing_user == None:
        session.close()
        raise HTTPException(status_code=404, detail="User not found")
    
    user_deleted = user_crud.delete_user(user_id)
    session.close()
    print("Deleted: ", user_deleted)
    
    return

@router.put("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)

async def update_user(user: UserUpdate = Body(...), token: str = Depends(oauth2_scheme)):    
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    user_name = token_verification(token)
    if user_name is None:
        raise credentials_exception
    
    #Verifica se o usuário existe
    user_crud = UserCRUD(session)
    existing_user = user_crud.read_user(user_id=user.id)
    print(existing_user)

    if existing_user == None:
        session.close()
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.email and user.password:
        print("Alterar tudo")
        user_crud.update_user(user_id=user.id, new_email=user.email, new_password=user.password)
    else:
        if user.email:
            print("alterar email")
            user_crud.update_user(user_id=user.id, new_email=user.email)
        if user.password:
            print("Alterar password")
            user_crud.update_user(user_id=user.id, new_password=user.password)

    return user