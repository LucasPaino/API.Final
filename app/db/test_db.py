from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

# Banco de dados de teste em memória
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# Cria todas as tabelas no banco de teste
Base.metadata.create_all(bind=engine)