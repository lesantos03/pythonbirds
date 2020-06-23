"""
você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1_ Atributo de dado velocidade
2_ Método acelerar, que deverá incrementar a velocidade de 1 unidade
3_ Método frear, que deverá decrementar a velocidade em 2 unidades

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos:
1_ Valor de direção com valores possíveis (norte, sul, leste, oeste)
2_ Método girar a direita
3_ Método girar a esquerda

    N
O       L
    S

    Exemplo:
    >>> #Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> #Testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_esquerda()
    >>> direcao.valor
    'Norte'

    >>> #Testando carro
    >>> carro = Carro(direcao,motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0


class Direcao:
    DIRECOES = ['Norte', 'Leste', 'Sul', 'Oeste']
    def __init__(self):
        self.dir_posicao = 0
        self.valor = self.DIRECOES[self.dir_posicao]

    def girar_direita(self):
        self.dir_posicao = (self.dir_posicao + 1) % len(self.DIRECOES)
        self.valor = self.DIRECOES[self.dir_posicao]

    def girar_esquerda(self):
        self.dir_posicao = (self.dir_posicao - 1) % len(self.DIRECOES)
        self.valor = self.DIRECOES[self.dir_posicao]