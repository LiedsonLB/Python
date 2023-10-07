import PySimpleGUI as sg

#layout
sg.theme('Reddit')
service = [
    [sg.Text('Digite sua conta: ')],
    [sg.Text(' ')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Button('serviço')]
]
layout = [
    [sg.Text('                     ') ,sg.Text('Digite sua conta: ')],
    [sg.Text('Número da conta:')],
    [sg.Input(key='conta')],
    [sg.Text('Senha:')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Text('')],
    [sg.Text('                    ') ,sg.Button('Entrar com conta')]
]

janela = sg.Window('Caixa - Conta', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['senha'] == '12345':
            print('welcome')
            janela = sg.Window('logado', service)