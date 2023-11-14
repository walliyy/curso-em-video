# Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.
op = 'S'
maior = menor = media = qntd = soma = num = 0

while op == 'S':
    num = int(input('Digite um número: '))
    if menor == 0:
        menor = num
    # if qntd == 1:
    #     maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    qntd += 1
    soma += num
    op = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
media = soma / qntd
print(f'O maior valor digitado foi {maior}', end='')
print(f', o menor valor digitado foi {menor}', end='')
print(f', a média dos valores é {media:.2f}!')