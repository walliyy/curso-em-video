''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do progframa, mostre:
-> A media de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres tem menos de 20 anos.'''
nome = []
idade = []
sexo = []

for c in range(1,5):
    nome.append(str(input('Digite seu nome: ')))
    idade.append(int(input('Digite sua idade: ')))
    sexo.append(str(input('Escolha M - Masculino ou F - Feminino: ')))
print(nome)
print(idade)
print(sexo)

print(f'A media de idade do grupo é {(sum(idade))/4}')