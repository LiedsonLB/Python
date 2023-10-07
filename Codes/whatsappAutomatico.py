import time

import pyautogui as pg


Nome = str(input('para quem você quer mandar uma mensagem ? '))
mensagem = str(input('o que quer escrever ? '))
pg.doubleClick(250, 800)
time.sleep(10)
pg.click(380, 200)
pg.typewrite(Nome)
time.sleep(1)
pg.press('enter')
time.sleep(1)
pg.typewrite(mensagem)
time.sleep(1)
pg.press('enter')
time.sleep(2)
pg.click(1140, 105)

time.sleep(1)
print('='*30)
print(' Mensagem enviada com sucesso ')
print('='*30)


#mensagens consecultivas
for i in range(0):
    pg.typewrite(mensagem)
    #adicione o press(enter)