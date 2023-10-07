# programa
nome = input('Digite o seu nome: ')


class usuario:
    def __init__(self, nome):
        self.nome = nome


user = usuario(nome)

if user.nome == 'myName':
    print('Óla, ', user.nome)
    print(' ')

alter_nome = input('deseja mudar o nome (y/n) ?: ')

if alter_nome == 'y':
    NewName = input('qual o novo nome: ')
    user.nome = NewName
    print('seu novo nome é ', user.nome)