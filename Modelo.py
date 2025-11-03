from sqlalchemy import Column, Integer, String, Date, Time, Text, ForeignKey, create_engine

from sqlalchemy.orm import declarative_base,relationship, sessionmaker

Base = declarative_base()


class Medicos(Base):
  __tablename__ = 'Medicos'

  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(100), nullable=False)
  especialidade = Column(String(100), nullable=False)
  telefone = Column(String(20))
  email = Column(String(100), unique=True)

  # Relacionamento: um médico pode ter várias consultas
  Consulta = relationship("Consultas", back_populates="Medicos")

class Pacientes(Base):
  __tablename__ = 'Pacientes'

  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(100), nullable=False)
  data_nascimento = Column(Date)
  telefone = Column(String(20))
  email = Column(String(100))

  # Relacionamento: um paciente pode ter várias consultas
  Consultas = relationship("Consultas", back_populates="Pacientes")

class Consultas(Base):
    __tablename__ = 'Consultas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_paciente = Column(Integer, ForeignKey('Pacientes.id'), nullable=False)
    id_medico = Column(Integer, ForeignKey('Medicos.id'), nullable=False)
    data_consulta = Column(Date, nullable=False)
    hora_consulta = Column(Time, nullable=False)
    descricao = Column(Text)
    status = Column(String(50), default='Agendada')

    # Relacionamentos bidirecionais
    Pacientes = relationship("Pacientes", back_populates="Consultas")
    Medicos = relationship("Medicos", back_populates="Consultas")
