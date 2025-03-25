from sqlalchemy import create_engine, MetaData, Table, select, text, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
import datetime
import json

# Substitua pelos detalhes da sua conexão
DATABASE_URL = "postgresql+psycopg2://michelmourao:PSWD@localhost:5432/michelmourao"

# Criando a engine de conexão
engine = create_engine(DATABASE_URL)

# Criando uma conexão
connection = engine.connect()

# Metadados do banco de dados
metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definindo o modelo da tabela
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)  # Usando datetime sem timezone

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

# Exemplo de uso
user_crud = UserCRUD(session)

# Criar um novo usuário
# new_user = user_crud.create_user("novo_usuario", "email@exemplo.com")
# print(f"Usuário criado: {new_user.username}")

#  Ler um usuário
# user = user_crud.read_user(user_id="5")
# print(f"Usuário encontrado: {user.username}, email: {user.email}")

# Atualizar um usuário
# updated_user = user_crud.update_user(user.id, new_username="NewMike")
# print(f"Usuário atualizado: {updated_user.username}")

# Deletar um usuário
# if user_crud.delete_user(user.id):
#     print("Usuário deletado com sucesso.")
# else:
#     print("Usuário não encontrado.")

users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Created At: {user.created_at}")

print(users)
# Fechar a sessão
session.close()
