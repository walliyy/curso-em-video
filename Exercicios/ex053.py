# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
frase = str(input('Digite aqui alguma coisa: ')).strip().upper() # strip tira o espaço
fSemEspaco = frase.replace(" ", "")
