# Crie um programa que leia um nome completo de uma pessoa e mostre:
# o nome com todas as letras maiusculas
# o nome com todas as letras minusculas
# quantas letras ao todo (sem considerar espaços)
# quantas letras tem o primeiro nome

nome = str(input('Informe o nome completo: ')).strip()

print('\nNome em Maiúsculas:', nome.upper())
print('\nNome em Maiúsculas:', nome.lower())
nome = nome.split()
print('\nQuantidade total de letras:', len(''.join(nome)))
# ou
# print('\nQuantidade total de letras: {}'.format(len(nome) - nome.count(' ')))
print('\nO primeiro nome tem {} letras'.format(len(nome[1])))