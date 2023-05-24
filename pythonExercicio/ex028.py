from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar num número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
# print('Pensei no número: {}'.format(computador))
jogador = int(input('Em que número eu pense? '))
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('Acertou!')
else:
    print('Errou! Computador gerou: {}'.format(computador))
