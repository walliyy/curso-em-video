''' Crie um programa que leia a idade de varias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados ianaragesser - 4796015283   
C) quantas mulheres tem menos de 20 anos'''
qntdMaiores = qntdHomens = qntdMulheres = 0

while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('ERRO! Digite M ou F: ')).upper().strip()[0]
    if idade > 18:
        qntdMaiores += 1
    if sexo == 'M':
        qntdHomens += 1
    if sexo == 'F' and idade < 20:
        qntdMulheres += 1
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Opção inválida! Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('PROGRAMA ENCERRADO')
print(f'Total de pessoas com mais de 18 anos: {qntdMaiores}.')
print(f'Ao todo temos {qntdHomens} homens cadastrados.')
print(f'E temos {qntdMulheres} mulheres com menos de 20 anos cadastradas.')