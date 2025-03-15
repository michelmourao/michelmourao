from sqlalchemy import select, text, Column, Integer, String, DateTime, Text, JSON, func
from datetime import datetime
from app.database import Base
from pydantic import BaseModel, EmailStr
from app.utils import get_password_hash
from typing import Optional
from typing import List

class UserModel:
        
    # Definindo o modelo da tabela usuários no BD
    class User(Base):
        __tablename__ = 'users'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False)
        plan = Column(String, nullable=False)
        created_at = Column(DateTime, default=datetime.now)  # Usando datetime sem timezone
        pswd = Column(String, nullable=False)

    # Definindo o modelo que retornará consulta de usuários na API
    class UserResponse(BaseModel):
        id: int
        email: str
        name: str
        plan: str
        created_at: datetime

        class Config:
            from_attributes = True #Informa o pydantic de que os dados são retorno de BD e facilita a conversão direta para .json

    # Definindo o modelo que receberá o json de criação de usuários
    class UserCreate(BaseModel):
        email: EmailStr
        name: str
        pswd: str
        plan: str

    # Definindo o modelo que receberá o json de update de usuários
    class UserUpdate(BaseModel):
        id: int
        email: Optional[EmailStr] = None
        name: Optional[str] = None
        pswd: Optional[str] = None
        plan: Optional[str] = None

    class UserCRUD:
        def __init__(self, session):
            self.session = session

        def create_user(self, email, name, plan, pswd):
            """Cria um novo usuário."""
            new_user = UserModel.User(email=email, name=name, plan=plan, pswd=get_password_hash(pswd))
            self.session.add(new_user)
            self.session.commit()
            return new_user

        def read_user(self, user_id=None, email=None):
            """Lê um usuário específico com base no ID ou username."""
            if user_id:
                return self.session.query(UserModel.User).filter_by(id=user_id).first()
            elif email:
                return self.session.query(UserModel.User).filter_by(email=email).first()

        def update_user(self, user_id,new_name=None, new_email=None, new_password=None, new_plan=None):
            """Atualiza as informações de um usuário específico."""
            user_to_update = self.session.query(UserModel.User).filter_by(id=user_id).first()
            if user_to_update:
                if new_name:
                    user_to_update.name = new_name
                if new_email:
                    user_to_update.email = new_email
                if new_password:
                    user_to_update.pswd = get_password_hash(new_password)
                if new_plan:
                    user_to_update.plan = new_plan
                self.session.commit()
                return user_to_update
            return None

        def delete_user(self, user_id):
            """Deleta um usuário específico."""
            user_to_delete = self.session.query(UserModel.User).filter_by(id=user_id).first()
            if user_to_delete:
                self.session.delete(user_to_delete)
                self.session.commit()
                return True
            return False

class AgentModel:
    # Definindo o modelo da tabela systemprompts no BD
    class Prompts(Base):
        __tablename__ = 'systemprompts'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        prompt = Column(String, nullable=False)

    # Definindo o modelo que retornará consulta de prompts na API
    class SystemPromptsResponse(BaseModel):
        id: int
        name: str
        prompt: str

        class Config:
            from_attributes = True #Informa o pydantic de que os dados são retorno de BD e facilita a conversão direta para .json

    # Definindo o modelo que receberá o json de criação de prompts
    class SystemPromptsCreate(BaseModel):
        name: str
        prompt: str

    # Definindo o modelo que receberá o json de update de prompts
    class SystemPromptsUpdate(BaseModel):
        id: int
        name: Optional[str] = None
        prompt: Optional[str] = None

    class SystemPromptsCRUD:
        def __init__(self, session):
            self.session = session

        def create_prompt(self, name, prompt):
            """Cria um novo prompt."""
            new_prompt = AgentModel.Prompts(name=name, prompt=prompt )
            self.session.add(new_prompt)
            self.session.commit()
            return new_prompt

        def read_prompt(self, prompt_id=None, name=None):
            """Lê um prompt específico com base no ID ou name."""
            if prompt_id:
                return self.session.query(AgentModel.Prompts).filter_by(id=prompt_id).first()
            elif name:
                return self.session.query(AgentModel.Prompts).filter_by(name=name).first()

        def update_prompt(self, prompt_id, new_name=None, new_prompt=None):
            """Atualiza as informações de um prompt específico."""
            prompt_to_update = self.session.query(AgentModel.Prompts).filter_by(id=prompt_id).first()
            if prompt_to_update:
                if new_name:
                    prompt_to_update.name = new_name
                if new_prompt:
                    prompt_to_update.prompt = new_prompt
                self.session.commit()
                return prompt_to_update
            return None

        def delete_prompt(self, prompt_id):
            """Deleta um prompt específico."""
            prompt_to_delete = self.session.query(AgentModel.Prompts).filter_by(id=prompt_id).first()
            if prompt_to_delete:
                self.session.delete(prompt_to_delete)
                self.session.commit()
                return True
            return False
    
    ########### CHAT SESSION ###########

    class ChatSession(Base):
        __tablename__ = "chatsessions"

        id = Column(Integer, primary_key=True, index=True)
        session_id = Column(String, unique=True, index=True)
        history = Column(JSON, nullable=False)
        user_id = Column(Integer, nullable=False)
        updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    class ChatSessionResponse(BaseModel):
        session_id: str
        history: List

        class Config:
            from_attributes = True #Informa o pydantic de que os dados são retorno de BD e facilita a conversão direta para .json

    class Message(BaseModel):
        content: str
        role: str  # "system", "user", "assistant"

    class ChatSessionUpdate(BaseModel):
        session_id: str
        history: List
    
    class ChatSessionCRUD:
        def __init__(self, session):
            self.session = session

        def create_chatsession(self, user_id, session_id, history):
            """Cria um novo chat."""
            new_chat = AgentModel.ChatSession(user_id=user_id, session_id=session_id, history=history)
            self.session.add(new_chat)
            self.session.commit()
            return new_chat

        def read_chatsession(self, user_id=None, session_id=None):
            """Lê um chat específico com base no ID."""
            if user_id:
                return self.session.query(AgentModel.ChatSession).filter_by(user_id=user_id).first()
            elif session_id:
                return self.session.query(AgentModel.ChatSession).filter_by(session_id=session_id).first()

        def update_chatsession(self, session_id, new_history):
            """Atualiza as informações de um chat específico."""
            chat_to_update = self.session.query(AgentModel.ChatSession).filter_by(session_id=session_id).first()
            if chat_to_update:
                chat_to_update.history = new_history
                self.session.commit()
                return chat_to_update
            return None

        def delete_chatsession(self, session_id):
            """Deleta um chat específico."""
            chat_to_delete = self.session.query(AgentModel.ChatSession).filter_by(session_id=session_id).first()
            if chat_to_delete:
                self.session.delete(chat_to_delete)
                self.session.commit()
                return True
            return False