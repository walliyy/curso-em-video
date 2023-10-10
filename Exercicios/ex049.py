# Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, so que utilizando um laço for.
num = int(input('Digite um numero inteiro: '))
for c in range(1, 11):
    print('{:<2} * {:>2} = {:>2}'.format(num, c, num*c))
print('FIM')