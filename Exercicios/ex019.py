# Um professor quer sortear um dos seus quarto alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))