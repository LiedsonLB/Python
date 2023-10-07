import time
import random

Num_card = ['1', "2", '3', '4', '5', '6', '7', '8', '9', '+4', '+2', 'block', 'reverse', 'change_color']
Type_color = ['red', 'blue', 'green', 'amarelo']

Deck_player = []
while len(Deck_player) < 9:
    carta = (random.choice(Num_card))
    if carta == ('+4', 'change_color'):
        Deck_player.append(carta)
    else:
        cor = random.choice(Type_color)
        New_card = carta + " " + cor
        Deck_player.append(New_card)
    if len(Deck_player) >= 9:
        time.sleep(1)
        print("Cartas do jogador 1: ")
        print(Deck_player)
