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