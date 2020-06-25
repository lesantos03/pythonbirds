class Pessoa:

    olhos = 2

    def __init__(self, nome = None, idade = None, *filhos):
        """
        Construtor da classe Pessoa
        :param nome: string
        :param idade: inteiro
        :param filhos: parâmetro múltiplo, recebe objeto Pessoa
        """
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Oi, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Mulher(Pessoa):
    def cumprimentar(self):
        cumprimentar_pai = super().cumprimentar()
        return f'{cumprimentar_pai}, beijo.'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    leticia = Pessoa('Letícia', 22)
    print(leticia.cumprimentar())
    print(f'{leticia.nome}, {leticia.idade} anos')
    jeane = Mulher('Jeane', 50, leticia)
    print(jeane.cumprimentar())
    jeane.sobrenome = 'Santos'
    print(jeane.__dict__)
    del jeane.sobrenome
    print(jeane.__dict__)
    for f in jeane.filhos:
        print(f.nome)

    print(Pessoa.olhos)
    print(jeane.olhos)
    jeane.olhos = 1
    print(jeane.__dict__)
    print(jeane.olhos)
    print(Pessoa.metodo_estatico(), leticia.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), leticia.nome_e_atributos_de_classe())

    print(isinstance(jeane,Pessoa))
    print(isinstance(jeane,Mulher))
    print(isinstance(leticia,Mulher))
    teste = Mutante()
    print(teste.olhos)