from sqlalchemy import create_engine, MetaData, Table, select, text, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg2://michelmourao:L10N]33!@localhost:5432/[HML]AI_Agent"

# Criando a engine de conexão
engine = create_engine(DATABASE_URL)

# Criando uma conexão
connection = engine.connect()

# Metadados do banco de dados
metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
