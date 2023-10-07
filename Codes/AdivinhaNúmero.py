import time
import random


def computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c'.lower():
        if low != 'c':
            numero = random.randint(low, high)
        else:
            numero = low
        time.sleep(1)
        feedback = input(f"o numero {numero} é maior (H), Menor(L) ou igual(C) ao que você está pensando: ")
        if feedback == 'H'.lower():
            high = numero - 1
        elif feedback == 'l'.lower():
            low = numero + 1

    print("numero correto")

computer(1000)
