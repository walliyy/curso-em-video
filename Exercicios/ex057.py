# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Informe seu sexo [M/F]: ').strip().upper()
while sexo not in 'MF':
    print("Sexo inválido!")
    sexo = input('Informe seu sexo [M/F]: ').strip().upper()
if sexo == 'M':
    print('Você é do sexo MASCULINO')
else:
    print('Você é do sexo FEMININO')