# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
num = int(input('Digite um numero inteiro: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('O numero digitado é {}, o dobro desse numero é {}, o triplo desse numero é {} e a raiz quadrada é {}'.format(num, dobro, triplo, raiz))