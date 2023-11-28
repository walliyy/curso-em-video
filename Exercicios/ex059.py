''' Crie um programa qque leia dois valores e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa

Seu programa deverá realixar a operação solicitada em cada caso
'''
from time import sleep

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
op = 0

print('Escolha uma opção no menu abaixo: ')
print('-=-' * 10)
while op != 5:
    op = int(input('''
[1] Somar os valores
[2] Multiplicar os valores
[3] Verificar qual é o maior
[4] Informar novos valores
[5] Sair do Programa \n
\n'''))
    if op == 1:
        print(f'A soma dos valores {n1} + {n2} é igual a {n1+n2}.')
    elif op == 2:
        print(f'O produto entre {n1} x {n2} é igual a {n1*n2}.')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é o maior número.')
        else:
            print(f'{n2} é o maior número.')
    elif op == 4:
        n1 = int(input('Informe o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))
    elif op == 5:
        print('Finalizando programa...')
        sleep(1)
        break
    else:
        print('\nOpção inválida! Tente novamente.\n')