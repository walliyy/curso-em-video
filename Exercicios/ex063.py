# Escreva um programa que leia um numero N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia de Fibonacci. 0 - 1 - 1 - 2 - 3 - 5 - 8
num = int(input('Digite quantos numeros deseja visualizar: '))

anterior = 0
atual = 1
cont = 0

print(anterior,'-', atual, end = " - ")

while cont < num - 2:
    proximo = anterior + atual
    print(proximo, end = " - ")
    cont += 1
    anterior = atual
    atual = proximo
print('FIM')