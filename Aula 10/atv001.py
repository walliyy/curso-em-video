# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e pela para o usuario tentar descobrir qual foi o número escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu.
import random

n = int(random.randrange(0,6))
g = int(input('Escolha um numero entre 0 e 5: '))

if g == n:
    print("Parabens! Voce acertou!")
else:
    print('Que pena, você perdeu!')
print('O numero escolhido foi {} e o numero correto é {}'.format(g, n))

# solucao do professor
from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar o numero
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pense?')) # jogador adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABENS!!! Você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(computador, jogador)) 