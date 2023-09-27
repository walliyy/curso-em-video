nome = input('Qual seu nome? ')

print('Prazer em te conhecer {:=>20}!'.format(nome), end=' ') #Alinhar a esquerda, 20 caracteres completando com =, o end faz preencher o final da linha com algo e tirar a quebra
print('Prazer em te conhecer \n{: = ^20} !'.format(nome)) #Alinhar ao meio, 20 caracteres completando com =, o \n quebra linha
print('Prazer em te conhecer {:=<20}!'.format(nome)) #Alinhar a direita, 20 caracteres completando com =