from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# String de conexão
DATABASE_URL = "postgresql://gomarket:gomarketpass@localhost:5432/gomarketdb"

# Criação da engine 
engine = create_engine(DATABASE_URL)

# Session para interagir com o Banco
Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para models herdarem
Base = declarative_base()