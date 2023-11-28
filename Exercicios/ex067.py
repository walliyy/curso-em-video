# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
cont = 1
while True:
    num = int(input('Deseja ver a Tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} X {cont} = {num * cont}')
        cont += 1
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO!')

# Solução do professor
while True:
    num = int(input('Deseja ver a Tabuada de qual valor? '))
    print('-'*30)
    if num < 0:
        break
    for c in range (1, 11):
        print(f'{num} X {c} = {num * c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO!')