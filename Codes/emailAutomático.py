import pyautogui as pg


remetente = str(input('Para quem você deseja enviar um email: '))
print('='*30)
print('Escolha uma das seguintes mensagens rápidas ou escreva o que deseja enviar:')
print('1: ola')
print('2: bom dia')
print('3: como vai ?')
print('4: tudo bem com você ?')
print('='*30)
assunto = (input('Qual mensagem deseja enviar: '))

mensagem_1 = str('Ola')
mensagem_2 = str('Bom dia')
mensagem_3 = str('Como vai ?')
mensagem_4 = str('Tudo bem com você')

if assunto == '1':
    assunto = mensagem_1
if assunto == '2':
    assunto = mensagem_2
if assunto == '3':
    assunto = mensagem_3
if assunto == '4':
    assunto = mensagem_4

print('='*30)
print(' Mensagem enviada com sucesso ')
print('='*30)