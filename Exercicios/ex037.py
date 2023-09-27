# Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Informe o numero inteiro a ser convertido: '))

converter = int(input('Escolha entre as opções de conversão abaixo: \n'
                      '1 - Converter para Binário\n'
                      '2 - Converter para Octal\n'
                      '3 - Converter para Hexadecimal\n'
                      'Sua opção: '))
if converter == 1:
    print('{} em BINÁRIO é igual á {}'.format(numero, bin(numero)[2:]))
elif converter == 2:
    print('{} em OCTAL é igual á {}'.format(numero, oct(numero)[2:]))
elif converter == 3:
    print ('{} em HEXADECIMAL é igual á {}'.format(numero, hex(numero)[2:]))
else:
    print("Opção inválida")