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
