from sqlalchemy import select, text, Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base
from pydantic import BaseModel

# Definindo o modelo da tabela no BD
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)  # Usando datetime sem timezone
    password_hash = Column(String, nullable=False)

# Definindo o modelo que retornará consulta de usuários na API
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True #Informa o pydantic de que os dados são retorno de BD e facilita a conversão direta para .json

class UserCRUD:
    def __init__(self, session):
        self.session = session

    def create_user(self, username, email):
        """Cria um novo usuário."""
        new_user = User(username=username, email=email)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def read_user(self, user_id=None, username=None):
        """Lê um usuário específico com base no ID ou username."""
        if user_id:
            return self.session.query(User).filter_by(id=user_id).first()
        elif username:
            return self.session.query(User).filter_by(username=username).first()
        return None

    def update_user(self, user_id, new_username=None, new_email=None):
        """Atualiza as informações de um usuário específico."""
        user_to_update = self.session.query(User).filter_by(id=user_id).first()
        if user_to_update:
            if new_username:
                user_to_update.username = new_username
            if new_email:
                user_to_update.email = new_email
            self.session.commit()
            return user_to_update
        return None

    def delete_user(self, user_id):
        """Deleta um usuário específico."""
        user_to_delete = self.session.query(User).filter_by(id=user_id).first()
        if user_to_delete:
            self.session.delete(user_to_delete)
            self.session.commit()
            return True
        return False

