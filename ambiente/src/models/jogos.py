from models.base import Base
from sqlalchemy import Column, Integer, String, Float

class Jogo(Base):
    __tablename__ = 'jogos'
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    plataforma = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)

    def __repr__ (self):
        return f'Nome do jogo = {self.nome}, plataforma = {self.plataforma}, preço de R${self.preco} e quantidade = {self.quantidade} unidades.'