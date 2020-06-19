class Pessoa:
    def __init__(self, nome = None, idade = None):
        """
        Construtor da classe Pessoa
        :param nome: string default none
        :param idade: inteiro defaultnone
        """
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return "Oi"

if __name__ == '__main__':
    pessoa = Pessoa('Letícia', 22)
    print(pessoa.cumprimentar())
    print(f'{pessoa.nome}, {pessoa.idade} anos')