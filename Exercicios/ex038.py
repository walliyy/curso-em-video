'''Escreva um programa que leia dois numeros inteiro e compar-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

if n1 > n2:
    print('O primeiro valor é maior')    
elif n1 < n2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
    