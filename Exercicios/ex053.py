# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input('Digite aqui alguma coisa: ')).strip().upper() # strip tira o espaço no inicio e final
fSemEspaco = frase.replace(" ", "") # replace substitiu os espaços por nada
# print(fSemEspaco)
# print(fSemEspaco[::-1])
if fSemEspaco == fSemEspaco[::-1]: # [::-1] essa parte do código pega toda a string contida na variavel e faz com que ela seja escrita de trás pra frente (passo -1)
    print('A frase digita é um palindromo!')
else:
    print('A frase digita não é um palindromo')

# Solução do professor

frase = str(input('Digite aqui alguma coisa: ')).strip().upper()
palavras = frase.split()  # split separa as palavras da string em lista
junto = ''.join(palavras)# join junta todas as palavras de forma unica
inverso = ''   # inverso vai receber o valor invertido das palavras
for letra in range(len(junto) -1, -1, -1):    # len conta quantos caracteres tem na variavel j
    inverso += junto[letra]     # + adiciona cada caracter ao fim da variável inversa
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('Não Temos um Palíndromo.')