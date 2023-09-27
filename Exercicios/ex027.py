# Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o ultimo nome separadamente.
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Primeiro: {}'.format(nome[0]))
print('Ultimo: {}'.format(nome[len(nome)-1]))