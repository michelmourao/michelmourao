from sqlalchemy import create_engine, MetaData, Table, select, text, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg2://michelmourao:12345678@localhost:5432/michelmourao"

# Criando a engine de conexão
engine = create_engine(DATABASE_URL)

# Criando uma conexão
connection = engine.connect()

# Metadados do banco de dados
metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# # Exemplo de uso
# user_crud = UserCRUD(session)

# # Criar um novo usuário
# new_user = user_crud.create_user("Teste1234", "teste1234@exemplo.com")
# print(f"Usuário criado: {new_user.username}")

# #  Ler um usuário
# user = user_crud.read_user(user_id="5")
# print(f"Usuário encontrado: {user.username}, email: {user.email}")

# # Atualizar um usuário
# updated_user = user_crud.update_user(user.id, new_username="NewMike")
# print(f"Usuário atualizado: {updated_user.username}")

# # Deletar um usuário
# if user_crud.delete_user(user.id):
#     print("Usuário deletado com sucesso.")
# else:
#     print("Usuário não encontrado.")

# users = session.query(User).all()
# for user in users:
#     print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Created At: {user.created_at}")

# print(users)
# # Fechar a sessão
# session.close()
