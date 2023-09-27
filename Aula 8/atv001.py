from math import sqrt # Importação especifica, quando for usar não precisa referenciar a biblioteca math.sqrt

num = int(input('Digite um numero: '))
raiz = sqrt(num)

print('\nA raiz de {} é igual a {:.2f}'.format(num, raiz))