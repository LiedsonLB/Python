import time

banco_dados = []
info_user = []
num_contas = 0

while True:

    usuario = input('Digite seu nome de Usuário: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    dados = ('Usuario: ' + usuario, 'email: ' + email, 'senha: ' + senha)
    banco_dados.append(dados)
    info_user.append(dados)
    num_contas = num_contas + 1
    time.sleep(2)
    print('Parabéns {}, sua conta foi cadastrada com sucesso'.format(usuario))
    ask_inform = input('Deseja ver suas informações(y/n): ')
    while ask_inform == 'pirulito':
        num_contas_info = 'numero de contas cadastradas: {}'.format(num_contas)
        print(num_contas_info)
        print(banco_dados)
        break

    if ask_inform == 'Y'.lower():
        print(banco_dados)
        break

    elif ask_inform == 'N'.lower():
        print('Ok, então')
