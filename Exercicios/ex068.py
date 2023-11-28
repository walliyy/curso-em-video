# Faça um programa que jogue por ou impar com o computador. O jogo só sera interrompido quanmdo o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

soma = jogador = computador = cont = 0

while True:
    op = str(input('Você escolhe Par ou Impar [P/I]: ')).upper().strip()[0]
    jogador = int(input('Digite um número: '))
    computador = randint(0,10)
    soma = computador + jogador
    if op in 'pP':
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
            print('-'*30)
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU IMPAR')
            print('-'*30)
            print('VOCÊ PERDEU!')
            break
    else:
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU IMPAR')
            print('-'*30)
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
            print('-'*30)
            print('VOCÊ PERDEU!')
            break
print(f'Fim do jogo, você teve um total de {cont} vitórias!')