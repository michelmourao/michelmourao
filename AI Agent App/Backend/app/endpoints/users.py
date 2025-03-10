from fastapi import APIRouter, Depends, HTTPException, status, Body
from app.auth import oauth2_scheme
from app.utils import token_verification
from app.models import UserModel
from app.database import session

UserCRUD = UserModel.UserCRUD
UserResponse = UserModel.UserResponse
UserCreate = UserModel.UserCreate
UserUpdate = UserModel.UserUpdate

router = APIRouter()

async def get_user_endpoint(user_id: int, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    user_crud = UserCRUD(session)
    user = user_crud.read_user(user_id=user_id)
    session.close()

    if user is not None:
        print(f"Usuário encontrado: {user.name}")
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
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    # Verifica se email está em uso
    existing_user = UserCRUD(session).read_user(email=user.email)
    if existing_user:
        session.close()
        raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = UserCRUD(session).create_user(email=user.email, name=user.name, plan=user.plan, pswd=user.pswd,)
    
    user_data = {
        "id": new_user.id,
        "email": new_user.email,
        "name": new_user.name,
        "plan": new_user.plan,
        "created_at": new_user.created_at
    }
    
    session.close()
    
    print('New user created!')

    return user_data

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_user(user_id: int, token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
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

    user_crud = UserCRUD(session)

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    #verifica se o novo email está em uso, caso tenha na requisição
    if user.email:
        print("Checando se o novo email existe...")
        existing_email = user_crud.read_user(email=user.email)
        print(existing_email)

        if existing_email == None:
            print("Email não existe...")
            session.close()
        else:
            raise HTTPException(status_code=404, detail="The email already exists, choose another one.")

    #Verifica se o usuário existe
    existing_user = user_crud.read_user(user_id=user.id)
    print(existing_user)

    if existing_user == None:
        session.close()
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.email and user.pswd and user.name and user.plan:
        print("Alterar tudo")
        user_crud.update_user(user_id=user.id, new_email=user.email, new_password=user.pswd, new_name=user.name, new_plan=user.plan)
    else:
        if user.email:
            print("alterar email")
            user_crud.update_user(user_id=user.id, new_email=user.email)
        if user.pswd:
            print("Alterar password")
            user_crud.update_user(user_id=user.id, new_password=user.pswd)
        if user.name:
            print("Alterar nome")
            user_crud.update_user(user_id=user.id, new_name=user.name)
        if user.plan:
            print("Alterar plano")
            user_crud.update_user(user_id=user.id, new_plan=user.plan)

    return user