# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
num = int(input('Digite um numero inteiro: '))

dobro = num * 2
triplo = num * 3
# raiz = num ** (1/2)
raiz = pow(num, (1/2))

print('O numero digitado é {}, o dobro desse numero é {}, o triplo desse numero é {} e a raiz quadrada é {}'.format(num, dobro, triplo, raiz))

# usando menos variaveis
# print('O numero digitado é {}, o dobro desse numero é {}, o triplo desse numero é {} e a raiz quadrada é {}'.format(num, (num*2), (num*3), (num**(1/2))))