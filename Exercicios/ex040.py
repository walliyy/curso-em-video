'''Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma uma mensagem no final, de acordo com a media atingida:
- media abaixo de 5.0: reprovado
- media entre 5.0 e 6.9 recuperação
- media 7.0 ou superior: aprovado'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5.0:
    print('REPROVADO')
elif media < 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')