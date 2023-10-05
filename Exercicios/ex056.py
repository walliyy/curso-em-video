''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do progframa, mostre:
-> A media de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres tem menos de 20 anos.'''
nome = []
idade = []
sexo = []

for c in range(1,5):
    nome.append(str(input('Digite seu nome: ')).upper())
    idade.append(int(input('Digite sua idade: ')))
    sexo.append(str(input('Escolha M - Masculino ou F - Feminino: ')).upper())

# for i, op in enumerate(sexo):
#     if op == 'M':
#         maior_idade = max(idade)
#         id_maior_idade = idade.index(maior_idade)
#         print(f'O homem mais velho é {nome[id_maior_idade]} que tem {maior_idade} anos')

masculino = 'M'
limite = 20
cont = 0 

if masculino in sexo:
    maior_idade = max(idade)
    id_maior_idade = idade.index(maior_idade)
elif masculino not in sexo:    
    for idades in idade:
        if idades > limite:
            cont += 1

print(f'-> A media de idade do grupo é {(sum(idade))/4}')
print(f'-> O homem mais velho é {nome[id_maior_idade]} que tem {maior_idade} anos')
print(f'-> A quantidade de mulheres menores que 20 é {cont}')