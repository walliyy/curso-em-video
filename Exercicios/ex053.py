# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input('Digite aqui alguma coisa: ')).strip().upper() # strip tira o espaço no inicio e final
fSemEspaco = frase.replace(" ", "") # replace substitiu os espaços por nada
# print(fSemEspaco)
# print(fSemEspaco[::-1])
if fSemEspaco == fSemEspaco[::-1]: # [::-1] essa parte do código pega toda a string contida na variavel e faz com que ela seja escrita de trás pra frente (passo -1)
    print('A frase digita é um palindromo!')
else:
    print('A frase digita não é um palindromo')