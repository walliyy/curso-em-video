import random
from time import sleep

computador = int(random.randrange(0,11))
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Escolha um numero entre 0 e 10: '))
print('PROCESSANDO...')

tentativas = 1

while jogador != computador:
    print('Que pena, você perdeu!')
    sleep(1)
    print('Vamos novamente?')
    sleep(1)
    jogador = int(input('Escolha um numero entre 0 e 10: '))
    tentativas += 1
sleep(1)    
print(f"Parabens! Voce acertou em {tentativas} tentativas!")
sleep(1)
print(f'O numero escolhido foi {jogador} e o numero correto é {computador}!')

# Solução do professor
from random import randint

computer = randint(0, 10)

print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é seu palpite? '))
    palpites += 1
    if player == computer:
        acertou = True
    else:
        if player < computer:
            print('Mais... tente mais uma vez.')
        elif player > computer:
            print('Menos... tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')