import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from Modelo import Consultas,Medicos,Pacientes,Base  # certifique-se que a classe Alunos está importada

# Carrega variáveis de ambiente
load_dotenv()

# Cria conexão com o banco
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
session.commit()  # confirma a alteração no banco



Base.metadata.create_all(engine)
