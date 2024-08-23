from sqlalchemy import create_engine, MetaData, Table, select, text, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
import datetime
import json

# Substitua pelos detalhes da sua conexão
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

# Definindo o modelo da tabela
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)
#     created_at = Column(String)

# Definindo o modelo da tabela
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)  # Usando datetime sem timezone

def new_user():
    # Criando um novo usuário
    new_user = User(username="mike", email="mike@exemplo.com")

    # Adicionando e confirmando (commit) a transação
    session.add(new_user)
    session.commit()

    return

new_user()

def delete_user():
    # Consultar o usuário que deseja deletar (por exemplo, pelo 'username')
    user_to_delete = session.query(User).filter_by(username="Mikee").first()

    # Verificar se o usuário existe
    if user_to_delete:
        # Deletar o usuário
        session.delete(user_to_delete)
        session.commit()  # Confirma a exclusão no banco de dados
        print(f"Usuário '{user_to_delete.username}' deletado com sucesso.")
    else:
        print("Usuário não encontrado.")

    return

#delete_user()

users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Created At: {user.created_at}")


def consult_json():

    # Realizando a consulta
    users = session.query(User).all()

    # Convertendo para lista de dicionários
    users_list = [
        {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'created_at': user.created_at
        }
        for user in users
    ]

    # Convertendo para JSON
    users_json = json.dumps(users_list, ensure_ascii=False, default=str)
    print(users_json)
    return

def orm_consult(users_table):
    print('ORM consult')
    # Selecionando todos os dados da tabela 'users'
    query = select(users_table).where(users_table.c.username == "Michel Mourão")

    # Executando a consulta
    result_set = connection.execute(query)

    # Extraindo os valores dos campos para variáveis
    user_data = result_set.fetchone()
    if user_data:
        user_id = user_data[0]
        username = user_data[1]
        email = user_data[2]
        created_at = user_data[3]

    # Agora você pode usar as variáveis como precisar
    print(f"ID: {user_id}, Username: {username}, Email: {email}, Created At: {created_at}")


    # Iterando pelos resultados
    for row in result_set:
        print(row)

    return

def query_consult(users_table):
    print('Query consult')
    # Selecionando todos os dados da tabela 'users'
    query = text("SELECT * FROM users WHERE username = :username")

    # Executando a consulta
    result_set = connection.execute(query, {"username": "Michel Mourão"})
    
    # Iterando pelos resultados
    for row in result_set:
        print(row)

    return



# Fechar a sessão
session.close()