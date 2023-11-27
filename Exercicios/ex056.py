''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do progframa, mostre:
-> A media de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres tem menos de 20 anos.'''
nome = []
idade = []
sexo = []

for c in range(1, 5):
    nome.append(str(input('Digite seu nome: ')).strip().upper())
    idade.append(int(input('Digite sua idade: ')))
    sexo.append(str(input('Escolha M - Masculino ou F - Feminino: ')).upper())

if len(nome) == len(idade) == len(sexo):
    cont = 0
    maior_idade = 0
    homem_mais_velho = ""

    for i in range(len(nome)):
        if sexo[i] == 'F' and idade[i] < 20:
            cont += 1

        if sexo[i] == 'M' and idade[i] > maior_idade:
            maior_idade = idade[i]
            homem_mais_velho = nome[i]

    print(f'-> A media de idade do grupo é {(sum(idade))/4}')
    if homem_mais_velho:
        print(f'-> O homem mais velho é {homem_mais_velho} que tem {maior_idade} anos')
    else:
        print('-> Não há homens cadastrados')
    print(f'-> A quantidade de mulheres menores que 20 é {cont}')
else:
    print('Erro')

# Solução do professor
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0
for p in range(1, 5):
    print(f'----- {p}º PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos')
print(f'O homem mais velho é o {nomeVelho}, com {maiorIdadeHomem} anos')
print(f'Ao todo são {totMulher20} mulher(es) com menos de 20 anos')