class Pessoa:
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
        return "Oi"

if __name__ == '__main__':
    leticia = Pessoa('Letícia', 22)
    print(leticia.cumprimentar())
    print(f'{leticia.nome}, {leticia.idade} anos')
    jeane = Pessoa('Jeane', 50, leticia)
    jeane.sobrenome = 'Santos'
    print(jeane.__dict__)
    del jeane.sobrenome
    print(jeane.__dict__)
    for f in jeane.filhos:
        print(f.nome)