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
        return "Oi"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


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

    print(Pessoa.olhos)
    print(jeane.olhos)
    jeane.olhos = 1
    print(jeane.__dict__)
    print(jeane.olhos)
    print(Pessoa.metodo_estatico(), leticia.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), leticia.nome_e_atributos_de_classe())