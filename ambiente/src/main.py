from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.jogos import Jogo

engine = create_engine('sqlite+pysqlite:///dadosJogos.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def inputJogos():
    jogo1 = Jogo(nome='DEAD SPACE REMAKE', plataforma='PS5', preco=350.00, quantidade=10)
    jogo2 = Jogo(nome='FORSPOKEN', plataforma='PC', preco=299.00, quantidade=8)
    jogo3 = Jogo(nome='DEAD ISLAND 2', plataforma='PS5', preco=350.00, quantidade=10)
    jogo4 = Jogo(nome='HOGWARTS LEGACY', plataforma='PC', preco=219.00, quantidade=7)
    jogo5 = Jogo(nome='WILD HEARTS', plataforma='XBox Series', preco=350.00, quantidade=7)
    jogo6 = Jogo(nome='RESIDENT EVIL 4', plataforma='PS5', preco=289.00, quantidade=10)
    jogo7 = Jogo(nome='THE LEGEND OF ZELDA: TEARS OF THE KINGDOM', plataforma='Switch', preco=350.00, quantidade=10)

    session.add(jogo1)
    session.add(jogo2)
    session.add(jogo3)
    session.add(jogo4)
    session.add(jogo5)
    session.add(jogo6)
    session.add(jogo7)

    session.commit()
    print('Jogos cadastrados com sucesso!')

def visualizarJogos():
    jogos = session.query(Jogo).all()
    if len(jogos) == 0:
        print('Não há jogos cadastrados!')
    else:
        for jogo in jogos:
            print(jogo)

def deletarJogos():
    jogos = session.query(Jogo).all()
    for jogo in jogos:
        session.delete(jogo)
    session.commit()

def userInput():
    while True:
        print('Cadastro e visualização de jogos:')
        print('- Envie 1 para cadastrar os jogos.')
        print('- Envie 2 para visualizar os jogos cadastrados.')
        print('- Envie 3 para deletar os jogos cadastrados.')
        opcao = int(input('Envie sua opção: '))
        if opcao == 1:
            inputJogos()
        elif opcao == 2:
            visualizarJogos()
        elif opcao == 3:
            deletarJogos()
        else:
            print('Opção inválida')



if __name__ == '__main__':
    userInput()