'''Refaça o desafio 35 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado
- Equilaterio: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))
# verificando se é um triângulo
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Forma triangulo!')
    if n1 == n2 == n3: # é o mesmo que colocar n1 == n2 and n2 == n3
        print('\033[4;36mTriângulo equilátero\033[m')
    elif n1 != n2 != n3 != n1:
        print('Triângulo escaleno')
    else:
        print('\033[7;36mTriângulo isósceles\033[m')
else:
    print('Não forma triangulo!')