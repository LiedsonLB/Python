import random
import time

Num_part = 0
lista_nomes = []

while True:
    input_nome = input("Nome do Participante: ")
    lista_nomes.append(input_nome)
    Num_part = Num_part + 1
    if Num_part >= 5:
        time.sleep(1)
        print("já temos 5 participantes")
        time.sleep(1)
        print(random.choice(lista_nomes))
        break
