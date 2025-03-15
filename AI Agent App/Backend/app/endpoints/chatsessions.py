from fastapi import APIRouter, Depends, HTTPException, status, Body
from app.auth import oauth2_scheme
from app.utils import token_verification, collect_id
from app.models import AgentModel, UserModel
from app.database import session
import uuid
import json

ChatSessionCRUD = AgentModel.ChatSessionCRUD
ChatSessionResponse = AgentModel.ChatSessionResponse
ChatSessionUpdate = AgentModel.ChatSessionUpdate
User = UserModel.User

router = APIRouter()

async def get_chat_endpoint(session_id: str, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    chat_crud = ChatSessionCRUD(session)
    chat = chat_crud.read_chatsession(session_id=session_id)
    session.close()

    if chat is not None:
        print(f"Chat encontrado: {chat.session_id}")
        # Converte JSON string para lista antes de retornar
        chat.history = json.loads(chat.history) if isinstance(chat.history, str) else chat.history
        return chat
    else:
        print("Chat não encontrado")
        raise HTTPException(status_code=404, detail="Chat not found")


@router.get("/{session_id}", response_model=ChatSessionResponse)

async def read_chat(chatsession = Depends(get_chat_endpoint)):
    return chatsession


@router.post("/", response_model=ChatSessionResponse, status_code=status.HTTP_201_CREATED)

async def create_chat(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    session_id = str(uuid.uuid4())

    # Verifica se session_id está em uso
    existing_chat = ChatSessionCRUD(session).read_chatsession(session_id=session_id)
    if existing_chat:
        session.close()
        raise HTTPException(status_code=400, detail="SessionId already registered.")
    
    user_id = collect_id(token=token)
    history = []
    new_chat = ChatSessionCRUD(session).create_chatsession(user_id=user_id, session_id=session_id, history=history)
    
    chat_data = {
        "session_id": new_chat.session_id,
        "history": new_chat.history,
    }
    
    session.close()
    
    print('New chat created!')

    return chat_data

@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)

async def delete_chat(session_id: str, token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception

    chat_crud = AgentModel.ChatSessionCRUD(session)

    #verifica se o chat existe
    existing_chat = chat_crud.read_chatsession(session_id=session_id)
    print(f'ChatSession found: {existing_chat}')

    if existing_chat == None:
        session.close()
        raise HTTPException(status_code=404, detail="Chat not found")
    
    chat_deleted = AgentModel.ChatSessionCRUD(session).delete_chatsession(session_id=session_id)
    session.close()
    print("Deleted: ", chat_deleted)
    
    return

@router.put("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)

async def update_chat(chat: ChatSessionUpdate = Body(...), token: str = Depends(oauth2_scheme)):    
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    #verifica o token
    sub = token_verification(token) #subscriber
    if sub is None:
        raise credentials_exception
    
    chat_crud = AgentModel.ChatSessionCRUD(session)

    #verifica se o chat existe
    existing_chat = chat_crud.read_chatsession(session_id=chat.session_id)
    print(f'ChatSession found: {existing_chat}')

    if existing_chat == None:
        session.close()
        raise HTTPException(status_code=404, detail="Chat not found")

    chat_crud.update_chatsession(session_id=chat.session_id, new_history=json.dumps(chat.history))

    return chat