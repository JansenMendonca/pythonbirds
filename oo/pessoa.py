class Pessoa:
    def __init__(self, nome = None, idade = 43):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Joao')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)